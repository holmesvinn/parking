# SVM for Traking Cars in Parking

Change working directory to hog_svm and download the dataset  
```
cd hog_svm
./get_dataset.sh
```

## Train the Support Vector Classifier
Run all the cells in `training.ipynb` and this will create two joblib files in the same directory

## Start the detection
Run all the cells in `detect.ipynb`

Update the window values for car slots in the `detect.ipynb` file. Change the values according to the video.
 
*Test Video in  `../test.mp4`*  
The windows (parking slots) for the `test.mp4` can be seen in the below image. **Only cars in these slots are detected.**
![Car slots](https://github.com/holmesvinn/parking/raw/master/parking_lot_img2.jpg)