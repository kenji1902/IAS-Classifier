import torch
import numpy as np
import os
import cv2
from .model import U2NET
from torch.autograd import Variable
from skimage import io, transform
from PIL import Image
from classifier.morphologicalMask import rgba2rgb,auto_crop
# Get The Current Directory
currentDir = os.path.dirname(__file__)

# Functions:
# Save Results


def save_output(inputdir, pred, d_dir, type):
    predict = pred
    predict = predict.squeeze()
    predict_np = predict.cpu().data.numpy()
    im = Image.fromarray(predict_np*255).convert('RGB')
    image = io.imread(inputdir)
    imo = im.resize((image.shape[1], image.shape[0]))
    pb_np = np.array(imo)
    if type == 'image':
        # Make and apply mask
        mask = pb_np[:, :, 0]
        mask = np.expand_dims(mask, axis=2)
        imo = np.concatenate((image, mask), axis=2)
        imo = Image.fromarray(imo, 'RGBA')
    imo = rgba2rgb(np.asarray(imo))
    imo,_ = auto_crop(imo)
    imo = cv2.resize(imo, (256,256), interpolation = cv2.INTER_AREA)
    cv2.imwrite(d_dir,cv2.cvtColor(imo, cv2.COLOR_BGR2RGB)) 
    
# Remove Background From Image (Generate Mask, and Final Results)


def removeBg(image,inputdir,resultsdir):
    # processing
    image = transform.resize(image, (320, 320), mode='constant')

    tmpImg = np.zeros((image.shape[0], image.shape[1], 3))

    tmpImg[:, :, 0] = (image[:, :, 0]-0.485)/0.229
    tmpImg[:, :, 1] = (image[:, :, 1]-0.456)/0.224
    tmpImg[:, :, 2] = (image[:, :, 2]-0.406)/0.225

    tmpImg = tmpImg.transpose((2, 0, 1))
    tmpImg = np.expand_dims(tmpImg, 0)
    image = torch.from_numpy(tmpImg)

    image = image.type(torch.FloatTensor)
    image = Variable(image)

    d1, d2, d3, d4, d5, d6, d7 = net(image)
    pred = d1[:, 0, :, :]
    ma = torch.max(pred)
    mi = torch.min(pred)
    dn = (pred-mi)/(ma-mi)
    pred = dn
    del d1, d2, d3, d4, d5, d6, d7
    save_output(inputdir, pred, resultsdir, 'image')
    return "---Success---"


# ------- Load Trained Model --------
print("---Loading Model---")
model_name = 'u2net'
model_dir = os.path.join(currentDir, 'saved_models',
                         model_name, model_name + '.pth')
net = U2NET(3, 1)
if torch.cuda.is_available():
    net.load_state_dict(torch.load(model_dir))
    net.cuda()
else:
    net.load_state_dict(torch.load(model_dir, map_location='cpu'))
print('u2net loaded')
# ------- Load Trained Model --------

