from .base import ZmBase
import cv2
import sys
import os

class ZmFace(ZmBase):

    def __init__(self, imagePath):
        self.option = []
        self.flag = []
        self.pixel = {}
        self.pixel_all={}
        return super().__init__(imagePath)

    def face_num(self, option):
    
        # Get user supplied values
        # imagePath = sys.argv[1]
        # imagePath = self.imagePath
        
        self.option = option
        print("Your Option:"+str(self.option))
        self.getHaarcascadeFile()

        cascPath = "haarcascade_frontalface_default.xml"

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(self.imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        print("Found {0} Faces! in the Picture".format(len(faces)))

        # judge the items
        for item in self.option:

            if item == '':
                self.flag.append('Null')
            elif item == 'Hide':
                self.flag.append(item)
            elif item == 'pixel':
                self.flag.append(item)

        if 'Null' in self.flag:
            # Draw a rectangle around the faces
            for(x, y, w, h) in faces:
                cv2.rectangle(image, (x,y), (x+w,y+w), (0, 255, 0), 2)

            cv2.imshow("Faces found", cv2.resize(image,(1024,768)))
            cv2.waitKey(0)
            
        else:
            if 'pixel' in self.flag and 'Hide'in self.flag:
                # OutPut the pixel of the Face
                for face_id in range(0,len(faces)):
                    for(x, y, w, h) in faces:
                        self.pixel['x'] = x
                        self.pixel['y'] = y
                        self.pixel['x+w'] = x+w
                        self.pixel['x+h'] = x+h
                        self.pixel_all[face_id+1]=self.pixel
                    self.pixel = {}
                print(self.pixel_all)
                print("Without imshow")
            elif 'Hide'in self.flag:
                print("Without imshow")


        pt_flag = self.get_platform_judge()        
        if(pt_flag==1):
            os.system("rm -rf haarcascade_frontalface_default.xml")
        else:
            os.system("del haarcascade_frontalface_default.xml")