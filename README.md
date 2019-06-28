# Zoomer

**author:RoWe98**

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

## How to run Zoomer

```bash
python test.py [filename]
or
Just add the filename in you Python code
```

## The main method for Zoomer

### 1.ZmFace

- **face_num**
**The Face analysis lib including counting the number of the person in the picture**

|Class_Method|Class_Method_describe|options|
|-|-|-|
|face_num|Get the face number of the picture|Hide, pixel, just blank|

**face_num options**

| option | describe |
| ------ | -------- |
|None|```option=[]``` Just output the OpenCV retangled image|
|Hide|Don't output OpenCV imshow|
|pixel|Output the pixel of the face|

**1.Option: None**
```
st2.jpg
Your Option:[]
Found 7 Faces! in the Picture
```
It would show the image processed by OpenCV in a new Window

**2.Option: Hide**
```
st2.jpg
Your Option:['Hide']
Found 7 Faces! in the Picture
Without imshow
```

**3.Option: Hide,pixel**
```
st2.jpg
Your Option:['Hide', 'pixel']
Found 7 Faces! in the Picture
{1: {'x': 935, 'y': 816, 'x+w': 1105, 'x+h': 1105}, 2: {'x': 935, 'y': 816, 'x+w': 1105, 'x+h': 1105}, 3: {'x': 935, 'y': 816, 'x+w': 1105, 'x+h': 1105}, 4: {'x': 935, 'y': 816, 'x+w': 1105, 'x+h': 1105}, 5: {'x': 935, 'y': 816, 'x+w': 1105, 'x+h': 1105}, 6: {'x': 935, 'y': 816, 'x+w': 1105, 'x+h': 1105}, 7: {'x': 935, 'y': 816, 'x+w': 1105, 'x+h': 1105}}
Without imshow
```

**4.face_num returns**

|returns|describe|
|-------|--------|
|face_pixel|The pixel of the each poeple in the picture|
|num_face|The number of the face in the picture|


## How to code with Zoomer

**Use Zoomer like this**

```python
# test.py
from zoomer import ZmFace
import sys
imagePath = sys.argv[1]
face_num_client = ZmFace(imagePath)
option = ['Hide','pixel']
option2 = ['Hide']
face_pixel, faces_num = face_num_client.face_num(option)
print(face_pixel)
print("Found {0} Faces! in the Picture".format(faces_num))

```

**Option can input more than 2 at once like ```option=['Hide','Pixel']```**


The current version of zoomer has only one function and it's class name is ```ZmFace```, Also it has a method named ```face_num()```, This method can get the face number of the picture you give to the program.


## Still Updating.....

## Contact

- E-Mail:wzx8551517@163.com
- [Blog](https://www.luoshaoqi.cn)
