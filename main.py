import scipy.misc 
from PIL import Image
import torch
import scipy.io as sio
import numpy as np
from bicubic import *
import scipy.misc 
import time
time_start = time.time()
time_end = time.time()
bicubic = bicubic()
img = np.array(Image.open('monarch.png'))
img = np.transpose(img,[2,0,1])
img = np.asarray(img, dtype = np.float32) / 255.0
img = torch.from_numpy(img).cuda().unsqueeze(0)
img_bicubic = bicubic(img, scale = 4)
img = img_bicubic[0]
img = np.transpose(img,[1,2,0])
time_end = time.time()
scipy.misc.toimage(img,cmin=0.0,cmax=1.0).save('mybicubic_4up.png')
print('totally cost',time_end-time_start)