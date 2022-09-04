from exif import Image
from .models import tempFileHandler

img_path = 'static/blobStorage/images/temp/kenji1902/IMG_20220521_155457.jpg'
def image_coordinates(image_path,fileName):
    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
            print(f"Was taken: {img.datetime_original}, and has coordinates:{coords}")
            return {
                'lat':coords[0],
                'lng':coords[1]
                }
        except AttributeError:
            print ('No Coordinates')
            obj = tempFileHandler.objects.filter(filename=fileName)
            return {
                'lat':obj[0].latitude,
                'lng':obj[0].longtitude
                }
    else:
        print (f'The Image {fileName} has no EXIF information')
        obj = tempFileHandler.objects.filter(filename=fileName)
        print(f"Does not have exif, retrieving gps loc:{obj[0].latitude}, {obj[0].longtitude}")
        return {
            'lat':obj[0].latitude,
            'lng':obj[0].longtitude
            }
    

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == 'S' or ref == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees    

