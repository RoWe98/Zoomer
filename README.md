# Zoomer

## What's Zoomer

- Zoomer is an opensource and cross-platform face recognition lib for python
- Zoomer is based on OpenCV and face_recognition
- Zoomer can let the human face compare and human face detect easily and fast
## The requirement lib for Zoomer

- OpenCV ```pip install opencv-python```
- face_recognition ```pip install face_recognition``` 

## How to download Zoomer

```bash
pip install Zoomer 
or
pip3 install Zoomer
```

## How to code with Zoomer

**Use Zoomer like this**

```python
# test.py
from zoomer import ZmFace
imagePath = sys.argv[1]
# imagePath = "Your file path"
face_num_client = ZmFace(imagePath)
option=[]  #Option List shown as followed
face_num_client.face_num(option)

```
| option | describe |
- | - |
None|```option=[]``` Just output the OpenCV retangle image
Hide|Don't output OpenCV imshow
pixel|Output the pixel of the face

**Option can input more than 2 at once like ```option=['Hide','Pixel']```**


The current version of zoomer has only one function and it's class name is ZmFace,Also it has a method named face_num(),This method can get the face number of the picture you give to the program.

## How to run Zoomer

```bash
python test.py [filename]
or
Just add the filename in you Python code
```

## The main method for Zoomer

- ZmFace The Face analysis lib including counting the number of the person in the picture

## Still Updating

## Contact

- E-Mail:wzx8551517@163.com
- [Blog](https://www.luoshaoqi.cn)
