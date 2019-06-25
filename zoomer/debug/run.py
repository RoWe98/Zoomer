from zoomer import face
import sys

imagePath = sys.argv[1]
face_num_client = face.ZmFace(imagePath)
option = []
face_num_client.face_num()


