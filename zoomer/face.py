from .base import ZmBase
import cv2
import sys

class ZmFace(ZmBase):

    def __init__(self, imagePath):
        return super().__init__(imagePath)

    def face_num(self):
    
        # Get user supplied values
        # imagePath = sys.argv[1]
        # imagePath = self.imagePath
        
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

        # Draw a rectangle around the faces
        for(x, y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w,y+w), (0, 255, 0), 2)

        cv2.imshow("Faces found", cv2.resize(image,(1024,768)))
        cv2.waitKey(0)
