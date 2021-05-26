import torch
import torch.nn.functional as F
from collections import OrderedDict
import numpy as np


class Classifier1(torch.nn.Module):

    def __init__(self, num_classes=40):
        super(Classifier1, self).__init__()

        self.head1 = torch.nn.Sequential(OrderedDict([
            ('head1_fc1', torch.nn.Linear(512, 256)),
            ('head1_relu1', torch.nn.ReLU()),
            ('head1_drop1', torch.nn.Dropout(p=0.4)),
            ('head1_fc2', torch.nn.Linear(256, 40)),
        ]))

    def forward(self, x):
        v = x[::,::,::8,::8,::8].contiguous()
        # print(v.size())
        pred1 = self.head1(v.view(v.size(0), -1))

        return pred1


class Classifier2(torch.nn.Module):

    def __init__(self, num_classes=40):
        super(Classifier2, self).__init__()

        self.stage2 = torch.nn.Sequential(OrderedDict([
            ('conv1', torch.nn.Conv3d(in_channels=1, out_channels=16, kernel_size=3)),
            ('bn1', torch.nn.BatchNorm3d(16)),
            ('lkrelu1', torch.nn.LeakyReLU()),
            ('pool1', torch.nn.MaxPool3d(2)),

            ('conv2', torch.nn.Conv3d(in_channels=16, out_channels=32, kernel_size=3)),
            ('bn2', torch.nn.BatchNorm3d(32)),
            ('lkrelu2', torch.nn.LeakyReLU()),
            ('pool2', torch.nn.MaxPool3d(2)),
        ]))

        self.stage2_maxpool = torch.nn.MaxPool3d(3)

        self.head2 = torch.nn.Sequential(OrderedDict([
            ('head2_drop0', torch.nn.Dropout(p=0.4)),
            ('head2_fc1', torch.nn.Linear(2048, 256)),
            ('head2_relu1', torch.nn.ReLU()),
            ('head2_drop1', torch.nn.Dropout(p=0.4)),
            ('head2_fc2', torch.nn.Linear(256, num_classes)),
        ]))

    def forward(self, x):
        x = x.unsqueeze(1)
        x = x[:, 0].contiguous()
        # print(x.shape)
        x = self.stage2(x)
        v = self.stage2_maxpool(x)
        # print(v.size())
        f2 = v.view(v.size(0), -1)
        f2 = self.head2(f2)
        return f2


class Classifier3(torch.nn.Module):

    def __init__(self, num_classes=40):
        super(Classifier3, self).__init__()

        self.stage2 = torch.nn.Sequential(OrderedDict([
            ('conv1', torch.nn.Conv3d(in_channels=1, out_channels=16, kernel_size=3)),
            ('bn1', torch.nn.BatchNorm3d(16)),
            ('lkrelu1', torch.nn.LeakyReLU()),
            ('pool1', torch.nn.MaxPool3d(2)),

            ('conv2', torch.nn.Conv3d(in_channels=16, out_channels=32, kernel_size=3)),
            ('bn2', torch.nn.BatchNorm3d(32)),
            ('lkrelu2', torch.nn.LeakyReLU()),
            ('pool2', torch.nn.MaxPool3d(2)),
        ]))

        self.head2 = torch.nn.Sequential(OrderedDict([
            ('head2_drop0', torch.nn.Dropout(p=0.4)),
            ('head2_fc1', torch.nn.Linear(2048, 256)),
            ('head2_relu1', torch.nn.ReLU()),
            ('head2_drop1', torch.nn.Dropout(p=0.4)),
            ('head2_fc2', torch.nn.Linear(256, num_classes)),
        ]))

        self.stage3 = torch.nn.Sequential(OrderedDict([
            ('conv3', torch.nn.Conv3d(in_channels=32, out_channels=64, kernel_size=3)),
            ('bn3', torch.nn.BatchNorm3d(64)),
            ('lkrelu3', torch.nn.LeakyReLU()),
            ('pool3', torch.nn.MaxPool3d(2)),
            ('conv4', torch.nn.Conv3d(in_channels=64, out_channels=128, kernel_size=3)),
            ('bn4', torch.nn.BatchNorm3d(128)),
            ('lkrelu4', torch.nn.LeakyReLU()),
            ('pool4', torch.nn.MaxPool3d(2)),
        ]))

        self.head3 = torch.nn.Sequential(OrderedDict([
            ('head3_drop0', torch.nn.Dropout(p=0.4)),
            ('head3_fc1', torch.nn.Linear(1024, 256)),
            ('head3_relu1', torch.nn.ReLU()),
            ('head3_drop2', torch.nn.Dropout(p=0.4)),
            ('head3_fc2', torch.nn.Linear(256, num_classes))
        ]))

    def forward(self, x):
        x = x.unsqueeze(1)
        x = x[:, 0].contiguous()
        # print(x.shape)
        x = self.stage2(x)
        v = self.stage3(x)
        # print(v.size())
        f3 = v.view(v.size(0), -1)
        f3 = self.head3(f3)
        return f3