import torch
import random
from torch.utils.data import Dataset, DataLoader

import numpy as np
import sys
import os
import re
import glob
sys.path.append("..")
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#print os.path.dirname(os.path.abspath(__file__))
#from utils import npytar
#from utils import npytar

class MVModelNet(Dataset):
    def __init__(self, shapenet_dir):
        self.objects = []

        for class_name in os.listdir(shapenet_dir):
            object_paths = glob.glob(os.path.join(shapenet_dir, class_name, '*.npy'))
            objects = list(set(('.'.join(obj.split('.')[:-2]) for obj in object_paths)))
            self.objects = self.objects + objects
    
    def __len__(self):
        return len(self.objects)

    def __getitem__(self, index):
        obj = self.objects[index]
        x = np.concatenate([
            np.load('%s.%03d.npy' % (obj, view_index))[None, None, ...]
            for view_index in range(1, 13)
        ], axis=0)
        y = int(os.path.basename(obj).split('.')[0]) - 1

        return torch.as_tensor(x, dtype=torch.float), torch.as_tensor(y, dtype=torch.long)


class NewMVModelNet32(Dataset):
    def __init__(self, shapenet_dir):
        self.object_paths = glob.glob(os.path.join(shapenet_dir, '*.npy'))
        random.shuffle(self.object_paths)

    def __len__(self):
        return len(self.object_paths)

    def __getitem__(self, index):
        object_path = self.object_paths[index]
        sdf = np.load(object_path)
        sdf = sdf.reshape((1,32,32,32,1))
        red=np.ones((1,32,32,32,1))
        blue=np.ones((1,32,32,32,1))
        over_0=sdf>=0
        below_0=sdf<0
        red[below_0]=0
        blue[over_0]=0
        sdf[below_0]*=-1
        x=np.concatenate([red, sdf, blue],axis=-1)
        y = int(os.path.basename(object_path).split('.')[0]) - 1

        return torch.as_tensor(x, dtype=torch.float), torch.as_tensor(y, dtype=torch.long)

class NewMVModelNet64(Dataset):
    def __init__(self, shapenet_dir):
        self.object_paths = glob.glob(os.path.join(shapenet_dir, '*.npy'))
        random.shuffle(self.object_paths)

    def __len__(self):
        return len(self.object_paths)

    def __getitem__(self, index):
        object_path = self.object_paths[index]
        sdf = np.load(object_path)
        sdf = sdf.reshape((1,64,64,64,1))
        red=np.ones((1,64,64,64,1))
        blue=np.ones((1,64,64,64,1))
        over_0=sdf>=0
        below_0=sdf<0
        red[below_0]=0
        blue[over_0]=0
        sdf[below_0]*=-1
        x=np.concatenate([red, sdf, blue],axis=-1)
        y = int(os.path.basename(object_path).split('.')[0]) - 1

        return torch.as_tensor(x, dtype=torch.float), torch.as_tensor(y, dtype=torch.long)


class NewMVModelNet(Dataset):
    def __init__(self, shapenet_dir):
        self.object_paths = glob.glob(os.path.join(shapenet_dir, '*.npy'))
        random.shuffle(self.object_paths)

    def __len__(self):
        return len(self.object_paths)

    def __getitem__(self, index):
        object_path = self.object_paths[index]
        x = np.load(object_path)
        # y = int(os.path.basename(object_path).split('.')[0]) - 1
        y = 0

        return torch.as_tensor(x, dtype=torch.float), torch.as_tensor(y, dtype=torch.long), object_path


class NewMVModelNet80(Dataset):
    def __init__(self, shapenet_dir):
        self.object_paths = glob.glob(os.path.join(shapenet_dir, '*.npy'))
        random.shuffle(self.object_paths)

    def __len__(self):
        return len(self.object_paths)

    def __getitem__(self, index):
        object_path = self.object_paths[index]
        x = np.load(object_path)
        y = int(os.path.basename(object_path).split('.')[0]) - 1

        return torch.as_tensor(x, dtype=torch.float), torch.as_tensor(y, dtype=torch.long), object_path



class NewMVModelNetxy(Dataset):
    def __init__(self, shapenet_dir):
        self.object_paths = glob.glob(os.path.join(shapenet_dir, '*.npy'))
        random.shuffle(self.object_paths)

    def __len__(self):
        return len(self.object_paths)

    def __getitem__(self, index):
        object_path = self.object_paths[index]
        x = np.load(object_path)
        label = int(os.path.basename(object_path).split('.')[0]) - 1
        y = np.zeros((40), dtype=float)
        y[label] = 1

        return torch.as_tensor(x, dtype=torch.float), torch.as_tensor(y, dtype=torch.float), torch.as_tensor(label, dtype=torch.long), object_path

if __name__ == '__main__':
    modelnet30 = MVModelNet("../data", "shapenet30_test.tar")
    print(__file__)
    print(os.path.dirname(__file__))
    print(len(modelnet30))
    print(modelnet30[123][0].shape, modelnet30[123][1])
    print(np.mean(modelnet30[123][0][np.where(modelnet30[123][0]!=0)]))
