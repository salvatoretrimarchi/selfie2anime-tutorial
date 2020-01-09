from PIL import Image
import os
import sys

paths = [
    "dataset/DATASET_NAME/testA/",
    "dataset/DATASET_NAME/testB/",
    "dataset/DATASET_NAME/trainA/",
    "dataset/DATASET_NAME/trainB/"
]


def resize():
    for path in paths:
        dirs = os.listdir(path)
        for item in dirs:
            if os.path.isfile(path+item):
                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                imResize = im.resize((256, 256), Image.ANTIALIAS)
                imResize.save(f + '.jpg', 'JPEG', quality=90)


resize()
