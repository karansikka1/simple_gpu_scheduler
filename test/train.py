import torch
import torchvision.models as models
import time
import os


num_files = len(os.listdir('log'))
print(f'Running {num_files+1}')
resnet18 = models.resnet18().cuda()
time.sleep(10)
os.system(f'touch log/{num_files+1}')


