#django utils
from django.http import JsonResponse
from django.shortcuts import render
from django.core.cache import cache
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import StreamingHttpResponse
from django.http import HttpResponse
import json
from io import BytesIO

#pytorch utils
import numpy as np
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
from torch.utils.data import DataLoader
from torch.autograd import Variable
import torch.nn.functional as F
import importlib
from .cascade.mvmodelnet import MVModelNet, NewMVModelNet

#OpenCv
import cv2 as cv

#python_pcl
import pcl

import os
import sys
from .cascade.ensemble_models import Classifier1
from .cascade.ensemble_models import Classifier2
from .cascade.ensemble_models import Classifier3

#make the dict ahead
categories = {"airplane":1,"bathtub":2,"bed":3,"bench":4,"bookshelf":5,"bottle":6,"bowl":7,"car":8,"chair":9,"cone":10,"cup":11,"curtain":12,"desk":13,"door":14,
              "dresser":15,"flower_pot":16,"glass_box":17,"guitar":18,"keyboard":19,"lamp":20,"laptop":21,"mantel":22,"monitor":23,"night_stand":24,"person":25,
              "piano":26,"plant":27,"radio":28,"range_hood":29,"sink":30,"sofa":31,"stairs":32,"stool":33,"table":34,"tent":35,"toilet":36,"tv_stand":37,"vase":38,
              "wardrobe":39,"xbox":40}

""""""""""""""""""""""""""""""
""""注意本后端需要使用绝对路径"""""
""""""""""""""""""""""""""""""

#load the dict of clf1
def getModel1():
    model1 = Classifier1()
    # model1_address = "./cascade/model/clf1.pth.tar"
    model1_address = "L:/Model_Rtrieval_System/csys/backend/cascade/model/clf1.pth.tar"
    model1.load_state_dict(torch.load(model1_address))
    return model1

#load the dict of clf2
def getModel2():
    model2 = Classifier2()
    model2_address = "L:/Model_Rtrieval_System/csys/backend/cascade/model/clf2.pth.tar"
    model2.load_state_dict(torch.load(model2_address)['model'])
    return model2

def getModel3():
    model3 = Classifier3()
    model3_address = "L:/Model_Rtrieval_System/csys/backend/cascade/model/clf3_2.pth.tar"
    model3.load_state_dict(torch.load(model3_address))
    return model3

def getThreshold():
    threshold1 = np.loadtxt('L:/Model_Rtrieval_System/csys/backend/cascade/threshold/threshold1.txt')
    threshold2 = np.loadtxt('L:/Model_Rtrieval_System/csys/backend/cascade/threshold/threshold2.txt')
    return threshold1,threshold2

#combine the post information to the datafile
def combinecs(category,serial):
    index = categories[category]
    finalstr = "{:03d}.{}_{:09d}.npy".format(index, category, serial)
    return finalstr

#get the result of model
def getResult(request):
    if request.method == 'POST':
        # load gpu
        cuda = torch.cuda.is_available()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        #load data
        modelData = request.FILES.get('file')
        modelFile = "L:/Model_Rtrieval_System/csys/backend/cascade/temp/"+modelData.name
        with open(modelFile,'wb') as f:
            f.write(modelData.read())
        processData = np.load(modelFile)
        test_set = NewMVModelNet("L:/Model_Rtrieval_System/csys/backend/cascade/temp")
        testLoader = DataLoader(test_set, batch_size=1, num_workers=0, drop_last=False)

        # load models
        # model1
        model1 = getModel1()
        model1.eval()
        # model2
        model2 = getModel2()
        model2.eval()
        # model3
        model3 = getModel3()
        model3.eval()
        if cuda:
            model1.to(device)
            model2.to(device)
            model3.to(device)

        # load threshold
        threshold1, threshold2 = getThreshold()

        #get result
        for i, (data, target, object_path) in enumerate(testLoader):
            if cuda:
                data = data.cuda()
            data = Variable(data)
            # print(data.shape)
            output1 = model1(data)
            score1 = F.softmax(output1, dim=1).max().item()
            pred1 = output1.data.max(1)[1].data
            if score1 >= threshold1[pred1]:
                # delete data cache
                os.remove("L:/Model_Rtrieval_System/csys/backend/cascade/temp/" + modelData.name)
                return JsonResponse({'category': pred1.item()})
            elif score1 < threshold1[pred1]:
                output2 = model2(data)
                score2 = F.softmax(output2, dim=1).max().item()
                pred2 = output2.data.max(1)[1].data
                if score2 >= threshold2[pred2]:
                    # delete data cache
                    os.remove("L:/Model_Rtrieval_System/csys/backend/cascade/temp/" + modelData.name)
                    return JsonResponse({'category': pred2.data.item()})
                elif score2 < threshold2[pred2]:
                    output3 = model3(data)
                    # score3 = F.softmax(output3,dim=1).max().item()
                    pred3 = output3.data.max(1)[1].data
                    # delete data cache
                    os.remove("L:/Model_Rtrieval_System/csys/backend/cascade/temp/" + modelData.name)
                    return JsonResponse({'category': pred3.item()})
        # else:
        #     return JsonResponse({'msg': 'input_empty'})
    else:
        return JsonResponse({'msg': 'POST_error'})

#文件读取
def read_file(file_name, chunk_size=512):
    with open(file_name, "rb") as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

#point_cloud 2 voxel
def point_cloud_to_volume_batch(point_clouds, vsize=32, radius=1.0, flatten=True):
    vol_list = []
    for b in range(point_clouds.shape[0]):
        vol = point_cloud_to_volume(np.squeeze(point_clouds[b, :, :]), vsize, radius)
        if flatten:
            vol_list.append(vol.flatten())
        else:
            vol_list.append(np.expand_dims(np.expand_dims(vol, -1), 0))
    if flatten:
        return np.vstack(vol_list)
    else:
        return np.concatenate(vol_list, 0)

#single point cloud 2 volume
def point_cloud_to_volume(points, vsize, radius=1.0):
    vol = np.zeros((vsize, vsize, vsize))
    voxel = 2 * radius / float(vsize)
    print('voxel: ', voxel)
    locations = (points + radius) / voxel
    print('locations: ', locations)
    locations = locations.astype(int)
    print('locations: ', locations)
    vol[locations[:, 0], locations[:, 1], locations[:, 2]] = 1.0
    return vol

#changeFormat
def changeFormat(request):
    file = request.FILES.get('file')
    filename = file.name
    tempStr = "L:/Model_Rtrieval_System/csys/backend/cascade/temp/"+filename
    with open(tempStr, 'wb') as f:
        f.write(file.read())

    #获得要转换的格式
    targetFormat = request.POST.get('target')
    namewithextend = filename.split('.', 1)[0]
    extend = filename.split('.',1)[1]

    datafile = pcl.load(tempStr)

    #initialize variable
    fullchangename = ''
    changeStr = ''

    # Format ply
    if targetFormat == 'ply':
        fullchangename = namewithextend+'.ply'
        changeStr = "L:/Model_Rtrieval_System/csys/backend/cascade/temp/"+fullchangename
        pcl.save(datafile,changeStr,"ply")

    # Format pcd
    if targetFormat == 'pcd':
        fullchangename = namewithextend + '.pcd'
        changeStr = "L:/Model_Rtrieval_System/csys/backend/cascade/temp/"+fullchangename
        pcl.save(datafile,changeStr,"pcd")

    #prepare response
    # response = StreamingHttpResponse(read_file(tempStr))
    response =  HttpResponse(read_file(changeStr))
    response["Content-Type"] = "application/octet-stream"
    response["Content-Disposition"] = 'attachment; filename={0}'.format(fullchangename)
    response["Access-Control-Expose-Headers"] = "Content-Disposition"

    #remove cache
    os.remove(tempStr)
    if  extend != targetFormat:
        os.remove(changeStr)
    return response

def test(request):
    if(request.method=='POST'):
        print("post information",request.FILES)
        modelData = request.FILES.get('file')
        print("data",modelData)

    return JsonResponse({'msg':"success"})
