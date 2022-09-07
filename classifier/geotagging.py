from exif import Image
from .models import tempFileHandler
from pprint import pprint
from PIL import Image
import piexif

img_path = 'static/blobStorage/images/raw/john_benedict/john_benedict-IMG_20220906_130218.jpg'
def image_coordinates(image_path,fileName):
    img = pilExif(image_path,'GPS')
    if img:
        try:
            coords = dms_to_dd(img)
            return {
                'status': 'has GPS Exif',
                'lat':coords[0],
                'lng':coords[1]
                }
        except ZeroDivisionError:
            obj = tempFileHandler.objects.filter(filename=fileName)
            return {
                'status':'GPS exif not present',
                'lat':obj[0].latitude,
                'lng':obj[0].longtitude
                }
    else:
        obj = tempFileHandler.objects.filter(filename=fileName)
        return {
            'status':'no Exif, using client\'s GPS',
            'lat':obj[0].latitude,
            'lng':obj[0].longtitude
            }
    

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == 'S' or ref == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees    



codec = 'ISO-8859-1'  # or latin-1
def exif_to_tag(exif_dict):
    exif_tag_dict = {}
    thumbnail = exif_dict.pop("thumbnail")
    if thumbnail is not None:
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

def pilExif(filename,type):
    
    exif_dict = piexif.load(filename)
    exif_dict = exif_to_tag(exif_dict)  
    return exif_dict[type]

def dms_to_dd(gps_exif):
     # convert the rational tuples by dividing each (numerator, denominator) pair
     lat = [n/d for n, d in gps_exif['GPSLatitude']]
     lon = [n/d for n, d in gps_exif['GPSLongitude']]

     # now you have lat and lon, which are lists of [degrees, minutes, seconds]
     # from the formula above
     dd_lat = lat[0] + lat[1]/60 + lat[2]/3600
     dd_lon = lon[0] + lon[1]/60 + lon[2]/3600

     # if latitude ref is 'S', make latitude negative
     if gps_exif['GPSLatitudeRef'] == 'S':
        dd_lat = -dd_lat
     
     # if longitude ref is 'W', make longitude negative
     if gps_exif['GPSLongitudeRef'] == 'W':
        dd_lon = -dd_lon

     return (dd_lat, dd_lon)

