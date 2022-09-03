from skimage.feature import hessian_matrix, hessian_matrix_eigvals
import cv2
import numpy as np
import matplotlib.pyplot as plt

def morphologicalMasking(image):
    processImg = segment_image(image)
    # processImg = sharpen_image(processImg)
    processImg = cv2.cvtColor(processImg,cv2.COLOR_RGB2GRAY)
    processImg = cv2.threshold(processImg, 1, 255, cv2.THRESH_BINARY)[1]
    processImg = np.reshape(processImg,(256,256,1))
    return processImg

def create_mask_for_image(image):
    '''
    Utility Function to create segmented morphological masks
    '''
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_hsv = np.array([20, 40, 20])
    upper_hsv = np.array([95, 255, 255])

    # find the green color 
    mask_green = cv2.inRange(image_hsv, (36,0,0), (86,255,255))
    # find the brown color
    mask_brown = cv2.inRange(image_hsv, (8, 60, 20), (30, 255, 200))
    # find the yellow color in the leaf
    mask_yellow = cv2.inRange(image_hsv, (21, 39, 64), (40, 255, 255))
    mask = cv2.bitwise_or(mask_green, mask_brown)
    mask = cv2.bitwise_or(mask, mask_yellow)

    # Bitwise-AND mask and original image
   


    # mask = cv2.inRange(image_hsv, lower_hsv, upper_hsv)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    return mask


def segment_image(image):
    '''
    Utility Function to apply segmented morphological masks
    '''
    mask = create_mask_for_image(image)
    output = cv2.bitwise_and(image, image, mask = mask)
    return output
 
def sharpen_image(image):
    '''
    Utility Function to sharpen processed images
    '''
    image_blurred = cv2.GaussianBlur(image, (0, 0), 1)
    # image_sharp = cv2.addWeighted(image, 1.5, image_blurred, 25.2, 0)
    image_sharp = cv2.addWeighted(image, 1.5, image_blurred, 2, 0)
    return image_sharp
def increase_brightness(img, value=100):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
# def convertImage(image):
#     h, w, c = image.shape
#     # append Alpha channel -- required for BGRA (Blue, Green, Red, Alpha)
#     image_bgra = np.concatenate([image, np.full((h, w, 1), 255, dtype=np.uint8)], axis=-1)
#     # create a mask where white pixels ([255, 255, 255]) are True
#     white = np.all(image == [255, 255, 255], axis=-1)
#     # change the values of Alpha to 0 for all the white pixels
#     image_bgra[white, -1] = 0
#     return np.array(image_bgra)
def convertImage(alpha):
    h, w = alpha.shape
    img = np.ones([h, w, 4], np.uint8) * (0, 0, 0, 255)
    img[:,:,3] = alpha
    return np.array(img)

    

def detect_ridges(image, sigma=1.0):
    grayscale_image =cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    ridge_filter = cv2.ximgproc.RidgeDetectionFilter_create(ddepth=cv2.CV_32FC1,ksize=5,scale=0.03)
    ridges = ridge_filter.getRidgeFilteredImage(grayscale_image)
    ridges = cv2.bitwise_not(ridges)
    ridges = cv2.cvtColor(ridges,cv2.COLOR_GRAY2RGBA)
    # ridges = convertImage(ridges)
    return ridges

def plot_images(*images,isRandom=True):
    plt.figure(figsize=(20, 10))
    n = len(images)
    if(n > 12):
      n = 12
    for i in range(n):
      rand = i
      if isRandom:
        rand=np.random.randint(0, n)
      ax = plt.subplot(3, 4, i + 1)
      plt.imshow(cv2.cvtColor(images[rand], cv2.COLOR_BGR2RGBA))


      plt.axis("off")

def rgba2rgb( rgba, background=(255,255,255) ):
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4, 'RGBA image has 4 channels.'

    rgb = np.zeros( (row, col, 3), dtype='float32' )
    r, g, b, a = rgba[:,:,0], rgba[:,:,1], rgba[:,:,2], rgba[:,:,3]

    a = np.asarray( a, dtype='float32' ) / 255.0

    R, G, B = background

    rgb[:,:,0] = r * a + (1.0 - a) * R
    rgb[:,:,1] = g * a + (1.0 - a) * G
    rgb[:,:,2] = b * a + (1.0 - a) * B

    return np.asarray( rgb, dtype='uint8' )

def overlay(background, foreground):
    # normalize alpha channels from 0-255 to 0-1
    alpha_background = background[:,:,3] / 255.0
    alpha_foreground = foreground[:,:,3] / 255.0

    # set adjusted colors
    for color in range(0, 3):
        background[:,:,color] = alpha_foreground * foreground[:,:,color] + \
            alpha_background * background[:,:,color] * (1 - alpha_foreground)

    # set adjusted alpha and denormalize back to 0-255
    background[:,:,3] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255
    return background

def removeBlurr(img):

  # grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # canny
  canned = cv2.Canny(gray, 100, 200)

  # dilate to close holes in lines
  kernel = np.ones((5,5),np.uint8)
  mask = cv2.dilate(canned, kernel, iterations = 1)

  # find contours
  # Opencv 3.4, if using a different major version (4.0 or 2.0), remove the first underscore
  contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  if not contours:
      return None
  # find big contours
  biggest_cntr = None
  biggest_area = 0
  for contour in contours:
      area = cv2.contourArea(contour)
      if area > biggest_area:
          biggest_area = area
          biggest_cntr = contour

  # draw contours
  crop_mask = np.zeros_like(mask)
  cv2.drawContours(crop_mask, [biggest_cntr], -1, (255), -1)

  # fill in holes
  # inverted
  inverted = cv2.bitwise_not(crop_mask)

  # contours again
  contours, _ = cv2.findContours(inverted, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  if not contours:
      return None
  # find small contours
  small_cntrs = []
  for contour in contours:
      area = cv2.contourArea(contour)
      if area < 20000:
          small_cntrs.append(contour)

  # draw on mask
  cv2.drawContours(crop_mask, small_cntrs, -1, (255), -1)

  # opening + median blur to smooth jaggies
  crop_mask = cv2.erode(crop_mask, kernel, iterations = 1)
  crop_mask = cv2.dilate(crop_mask, kernel, iterations = 1)
  crop_mask = cv2.medianBlur(crop_mask, 5)

  # crop image
  crop = np.zeros_like(img)
  crop[crop_mask == 255] = img[crop_mask == 255]

  # show
  # cv2_imshow(img);
  # cv2_imshow(gray);
  # cv2_imshow(canned);
  # cv2_imshow(crop_mask);
  # cv2_imshow(crop);
  # cv2.waitKey(0);
  return crop