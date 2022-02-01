'''
Created on Feb 13, 2020

@author: eljurros
'''
'''
Created on Mar 20, 2019

@author: eljurros
'''
from DataSEt_Classes import SegThorDS, SegmentationPair2D_Prostate, Prostate
from Label_Estimate_Helper_Functions import extract_bbox, rect_mask, get__mask, Get_Upper_Lower_boundaries
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

typ = 'ROOT'
root_path = '/media/eljurros/Transcend/Decathlone/Task02_Heart'
nifty_root = os.path.join(root_path, 'nifty')
fold_root = os.path.join(nifty_root, 'FOLD_2')
if os.path.exists(os.path.join(fold_root)) is False:
    os.mkdir(fold_root)
    os.mkdir(os.path.join(fold_root, 'train'))
    os.mkdir(os.path.join(fold_root, 'val'))
inner_arr = []
outer_arr = []
#Prostate_ds = SegThorDS(root_dir=os.path.join(root_path, typ))
Prostate_ds = Prostate(root_path, typ)

v_nb = 0
for i, patient_path in enumerate(Prostate_ds.filename_pairs):
    print('copying ', patient_path)
    patient_name = os.path.basename(patient_path[0])
    input_filename, gt_filename, cntr_filename = patient_path[0], patient_path[1], patient_path[2]

    i = random.uniform(0, 1)

    if i < 0.2 and v_nb < 4:
        path = os.path.join(fold_root, 'val', patient_name.split('.nii.gz')[0])
        v_nb = v_nb +1

    else:
        path = os.path.join(fold_root,'train', patient_name.split('.nii.gz')[0])


    if os.path.exists(path) is False:
            os.mkdir(path)
    shutil.copy(input_filename, path)
    shutil.copy(gt_filename, path)
    shutil.copy(cntr_filename, path)
    
        







        
