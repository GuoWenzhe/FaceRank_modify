# FaceRank_modify
this project was modify by this version: https://github.com/fendouai/FaceRank  

## data uploaded:
http://pan.baidu.com/s/1qYSFE9Y   password: ubaw  

## input type:
the picture name should be named as 1-3.jpg, means rank 1, 3st train picture  

## Run
After you installed TensorFlow:  
```python
#using find_face_in_picture to find the face in the whole picture and resize the face to 128*128  
python find_faces_in_picture.py ./data/input_image/ ./data/resize_image/  

#using tensorflow train model and save the model to model dir.  
/home/hmx/neural-enhance-master/python-3.4/bin/python3 train_model.py     
```

## Test
After you run the train_model.py ,just run the run_model.py to test.  
```python
#the same as train step1 
python find_faces_in_picture.py ./data/test_input/ ./data/test_resize/      
#using run_model_one.py to test  
/home/hmx/neural-enhance-master/python-3.4/bin/python3 run_model_one.py   
```
