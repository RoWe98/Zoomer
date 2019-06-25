from face import ZmFace
import sys

imagePath = sys.argv[1]
face_num_client = ZmFace(imagePath)
option = ['Hide','pixel']
option2 = ['Hide']
face_num_client.face_num(option2)


