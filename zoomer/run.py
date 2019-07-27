from face import ZmFace
import sys

imagePath = "/Users/rex/Desktop/Code/Intelligence_classroom/image/1normal4.jpg"
face_num_client = ZmFace(imagePath)
option = ['Hide','pixel']
option2 = ['Hide']
face_pixel, faces_num = face_num_client.face_num(option)
print(face_pixel)
print("Found {0} Faces! in the Picture".format(faces_num))


