from django.test import TestCase

# Create your tests here.
import numpy as np
import morphologicalMask as morphMask
import cv2
# import keyboard
# cam = cv2.VideoCapture(2)
# cv2.namedWindow("video", cv2.WINDOW_NORMAL)    
# cv2.resizeWindow("video", 960, 540)
# while True:

#     check, frame = cam.read()
#     frame = cv2.resize(frame, (256,256), interpolation = cv2.INTER_AREA)
#     processImg = morphMask.morphologicalMasking(frame)
#     processImg = np.concatenate((np.array(frame),np.array(processImg)),axis=2)
#     processImg = morphMask.rgba2rgb(np.array(processImg))
#     cv2.imshow('video', processImg)

#     key = cv2.waitKey(1)
#     if keyboard.is_pressed('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()

# from exif import Image
# image_path = 'static/blobStorage/images/temp/kenji/kenji-john_benedict-20220906_125642_copy_copy_copy_copy_copy.jpg'
# with open(image_path, 'rb') as src:
#     img = Image(src)
# print(img)

from pprint import pprint
from PIL import Image
import piexif

codec = 'ISO-8859-1'  # or latin-1
def exif_to_tag(exif_dict):
    exif_tag_dict = {}
    thumbnail = exif_dict.pop("thumbnail")
    if thumbnail is not None:
        with open("thumbnail.jpg", "wb+") as f:
            f.write(thumbnail)
    
        exif_tag_dict['thumbnail'] = thumbnail.decode(codec)

    for ifd in exif_dict:
        exif_tag_dict[ifd] = {}
        for tag in exif_dict[ifd]:
            try:
                element = exif_dict[ifd][tag].decode(codec)

            except AttributeError:
                element = exif_dict[ifd][tag]

            exif_tag_dict[ifd][piexif.TAGS[ifd][tag]["name"]] = element

    return exif_tag_dict

def main():
    filename = 'static/blobStorage/images/raw/john_benedict/john_benedict-20220906_125700.jpg'  # obviously one of your own pictures
    # im = Image.open(filename)
    
    # exif_dict = piexif.load(im.info.get('exif'))
    
    exif_dict = piexif.load(filename)
    exif_dict = exif_to_tag(exif_dict)  

    if exif_dict['GPS']:
        pprint(exif_dict['GPS'])

if __name__ == '__main__':
   main()