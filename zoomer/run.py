from face import ZmFace
import sys

imagePath = sys.argv[1]
face_num_client = ZmFace(imagePath)
face_num_client.face_num()


