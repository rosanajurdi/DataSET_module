# DataSET_module
Module containing dataset functionalities. 
1. SPlit datasets into folds 
2. Generate dataset characteristics and meta properties
3.Generating distance maps, computing border irregularity index
4. Dataset Visualizations

Note: Right now the only public scripts are the ones used to split the dataset into folds. 

# Requirements:
1. cv2 
2. torch, 
3. numpy, 
4. scipy, 
5. random 
6. 
 

KFOLD-Split_Dataset: Script to divide the data into folds, 
- Import the required dataset class from DataSEt_Classes and initialize an instance of the class ds. 
- place the data ensembles (imagesTr, labelsTr) from decathlon in nifty/root.

## variables to initialize
typ = 'ROOT': the root folder you want your downloaded dataset to be in. preferably place it in ROOT. 
root_path: the root directory leading to your data.
fold: the name of the target fold 
nb_val: the number of validation samples (recommended to be 20% of the total training set)
