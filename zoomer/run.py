from .face import ZmFace
import sys

imagePath = sys.argv[1]
face_num_client = ZmFace(imagePath)
option = ['Hide','pixel']
face_num_client.face_num(option)


