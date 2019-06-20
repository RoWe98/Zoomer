from base import ZmBase
import sys

imagePath = sys.argv[1]
zm = ZmBase(imagePath)
zm.getHaarcascadeFile()
