from PIL import Image
import face_recognition
import os
import cv2
import sys
import numpy as np
print("h")

INPUT_DIR = sys.argv[1]
OUTPUT_DIR = sys.argv[2]

def find_and_save_face(web_file,face_file):
    # Load the jpg file into a numpy array
    #image = face_recognition.load_image_file(web_file)
    image = cv2.imread(web_file)
    image1 = np.zeros(image.shape,np.uint8)
    image1 = image.copy()

    print(image.dtype)
    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image1)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    if (len(face_locations)>1):
         print("there are too many faces in this photograph.")
         return
    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]

        resize_image = cv2.resize(face_image,(128,128))
        cv2.imwrite(face_file, resize_image)
        #pil_image = Image.fromarray(resize_image)
        #pil_image.save(face_file)
print("h")
list = os.listdir(INPUT_DIR)
print(list)

def get_face():
    for image in list:
        id_tag = image.find(".")
        name=image[0:id_tag]
        print(name)

        web_file = INPUT_DIR +image
        face_file= OUTPUT_DIR +name+".jpg"

        im=Image.open(INPUT_DIR+image)
        try:
            find_and_save_face(web_file, face_file)
        except:
            print("fail")

if __name__ == '__main__':
    get_face()
