from .base import ZmBase
import cv2
import sys
import os
import face_recognition


class ZmFace(ZmBase):

    def __init__(self, imagePath):
        self.option = []
        self.flag = []
        self.pixel = {}
        self.pixel_all={}
        self.pixel_list = []
        return super().__init__(imagePath)

    # def face_num(self, option):
    
    #     # Get user supplied values
    #     # imagePath = sys.argv[1]
    #     # imagePath = self.imagePath
        
    #     self.option = option
    #     print("Your Option:"+str(self.option))
    #     self.getHaarcascadeFile()

    #     cascPath = "haarcascade_frontalface_default.xml"

    #     # Create the haar cascade
    #     faceCascade = cv2.CascadeClassifier(cascPath)

    #     # Read the image
    #     image = cv2.imread(self.imagePath)
    #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #     # Detect faces in image
    #     faces = faceCascade.detectMultiScale(
    #         gray,
    #         scaleFactor=1.1,
    #         minNeighbors=5,
    #         minSize=(30, 30)
    #     )
    #     print("Found {0} Faces! in the Picture".format(len(faces)))

    #     # judge the items and judge options
    #     if len(self.option) == 0:
    #         self.flag.append('Null')

    #     else:
    #         for item in self.option:

    #             if item == 'Hide':
    #                 self.flag.append(item)
    #             elif item == 'pixel':
    #                 self.flag.append(item)

    #     if 'Null' in self.flag:
    #         # Draw a rectangle around the faces
    #         for(x, y, w, h) in faces:
    #             cv2.rectangle(image, (x,y), (x+w,y+w), (0, 255, 0), 2)

    #         cv2.imshow("Faces found", cv2.resize(image,(1024,768)))
    #         cv2.waitKey(0)
            
    #     else:
    #         if 'pixel' in self.flag and 'Hide'in self.flag:
    #             # OutPut the pixel of the Face
    #             pixel_num = 0
    #             for(x, y, w, h) in faces:
    #                 self.pixel['x'] = x
    #                 self.pixel['y'] = y
    #                 self.pixel['x+w'] = x+w
    #                 self.pixel['x+h'] = x+h
    #                 self.pixel_all[pixel_num+1]=str(self.pixel)
    #                 pixel_num = pixel_num + 1
    #             #print(self.pixel_all)
    #             print("Without imshow")
    #             self.clean()
    #             return self.pixel_all, len(faces)
    #         elif 'Hide'in self.flag:
    #             print("Without imshow")

    def face_num(self, option):

        self.option = option
        print("Your Option:"+str(self.option))
        image = face_recognition.load_image_file(self.imagePath)

        face_loaction = face_recognition.face_locations(image)

        print("Found {0} Faces!".format(len(face_loaction)))

        # Read the image with openCV

        image = cv2.imread(self.imagePath)

        # Draw a rectangle around the faces
        for(top, right, bottom, left) in face_loaction:
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Faces found", cv2.resize(image,(1024,768)))
        cv2.waitKey(0)

    def clean(self): 
        pt_flag = self.get_platform_judge()        
        if pt_flag == 1:
            os.system("rm -rf haarcascade_frontalface_default.xml")
        else:
            os.system("del haarcascade_frontalface_default.xml")




