First , we are taking an over view of the datasets

standard :
https://drive.google.com/drive/folders/1G8g8TxVekRej4_RYqEY_akOFUKBDa9u7?usp=sharing

Non-Standard:
https://drive.google.com/drive/folders/1hIKDmkSVXbSwbjxUq5VIjHxKy2-W17m2?usp=sharing

Both of them have to folders :

JPEGImages : Which contain the Images of cars
Annotations : Which contain the annotation of the Plates

---------------------------------------------------------------------------

Task 1 >> Load the data into fiftyone tool :

Fiftyone Tool : it provides us with a graphical interface to investigate our data and make analysis . One important function is that it exports the dataset and annotation in diffrent formats which may be needed by diffrent models.

Steps :

1- we tried to run the quick start notebook on colab .
    -  for some reason it didn't work

2- we tried to run the quick start on local machine and it worked . [ All fiftyone work is in the notebook "Fiftyone-dataset.ipynb" ]

3- Trying to load the dataset "Standard" to see how the tool works
    - The fiftyone tool accepts many formats of Images and annotation formats ( you can find them here : https://voxel51.com/docs/fiftyone/user_guide/dataset_creation/datasets.html#vocdetectiondataset-import  , one of them is VOC which have annotations in xml file which is our case .

4- Importing the dataset to the tool and test it .

5- After that , trying to export the data in COCO format , which used with the detection model we want to use .

6- After knowing how the tool work , we start to processing the full dataset
    - We decided to label the data to 2 classes : Standard and Non-standard , instead of Plate .
    - To do that we need to go over all the annotation file and change the 'name' element in the 'object' element to either 'standard' or 'non-standard' . [ Code is in helpers folder "Change-Label.py" ]
    - After that we find some Images that don't have correct annotation ( missing coordainiates of the plate box) . Solving this problem manually by use a script that shows the image and find the (x,y) coordainiates of where we click the mouse , so click on the boarders of the plate and record (xmin,xmax,ymin,ymax). [ Code is in helpers folder "Annotate.py" ]
    - After combining the two datasets we find that there are some Images that don't have an annotation file , we simply exclude them as there were like 81 images which is only 1.8% . [ Code is in helpers folder "missedAnn.py" ]

7- After that we entering the data to the fiftyone tool and export it as COCO format
    - Here we find an ununderstandable problem , as all images have a label either 'standard' or 'non-standard' , the tool reads some images as Plate while they are set to one of the classes.
    - To solve this problem we force the fiftyone tool to export images in the two main classes and ignoring other labels ( this also does have approxmitely no effect on the dataset size)

---------------------------------------------------------------

Task 2 >> Train the model using MMdetection :


8- After preperaing the dataset , we start to use mmdetection  : https://github.com/open-mmlab/mmdetection
    it is a tool used to ease the training of many models like YOLO, Fast R-CNN , etc.,

9- Starting by run the tutriol provided , and uploading the data set to drive .

10- The tutorial starts by setting up the environment and setup dependecies , after that it gives an example on a dataset and how to transfer it to the structure that could be used .
    - As our dataset is already in COCO format we import it directly to the tool
    - The tutorial didn't clarify how to edit the model if your data is already correctly formatted so after some research we find a tutorial which shows how to edit the config file and run the model :
    https://mirror-medium.com/?m=https%3A%2F%2Fmedium.com%2Fm%2Fglobal-identity%3FredirectUrl%3Dhttps%253A%252F%252Ftowardsdatascience.com%252Fmmdetection-tutorial-an-end2end-state-of-the-art-object-detection-library-59064deeada3
11- After that we run the model for training
    - There were some problems :
        - We need to split the data to train , test , validate
