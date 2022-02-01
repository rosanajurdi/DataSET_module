'''
Created on Feb 13, 2020

@author: eljurros
'''
'''
Created on Mar 20, 2019

@author: eljurros
'''
from DataSET_module.DataSEt_Classes import SegThorDS, SegmentationPair2D_Prostate, Prostate
from DataSET_module.Label_Estimate_Helper_Functions import extract_bbox, rect_mask, get__mask, Get_Upper_Lower_boundaries
from torchvision import transforms
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import imageio
import h5py
import sys
import os
import shutil
import random
sys.path.append('../medicaltorch-0.2')
sys.path.append('/home/eljurros/spare-workplace/Multi_Organ_Segmentation/DataSet_Functions')

root = '/media/eljurros/Transcend/CoordConv/SEGTHOR/segthor/Thomas_Segthor'




for _,_, patients in os.walk(os.path.join(root,'test', 'img' )):
    for patient in patients:
        with open(os.path.join(os.path.join(root,'test.txt')), 'a') as the_file:
            the_file.write(patient)
            the_file.write('\n')
    
    

    
        







        
