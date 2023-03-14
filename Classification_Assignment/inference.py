import cv2
import time
import torch
import numpy as np
from models import BaseFeatureExtractor

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# checkpoints link
# https://drive.google.com/drive/folders/1y9EPmDUeXOYRmYSSYEd5Vo0XarIkEBsM?usp=sharing
onnx_model_path = "checkpoints/swin/best_model.onnx"

CLASSES = ['Audi.common', 'BMW.common', 'Chevrolet.common', 'Datsun.common', 'Fiat.common',
         'Ford.common', 'Honda.common', 'Hyundai.common', 'ISUZU.common', 'Jaguar.frontal', 
         'Jaguar.rear', 'Jeep.common', 'Kia.common', 'Kia.new', 'MG-Motor.common', 'Mahindra.common', 
         'Maruti-Suzuki.common', 'Mercedes-Benz.common', 'Mitsubishi.common', 'Nissan.common', 
         'Renault.common', 'Skoda.common', 'Tata.common', 'Tata.text', 'Toyota.common', 
         'Volkswagen.common', 'Volvo.frontal', 'unknown']


# dummy_input = torch.randn(1, 3, 224, 224)
# model = BaseFeatureExtractor('swin', n_class=28)
# model_path = 'checkpoints/swin/best_model.pt'
# ckpt = torch.load(model_path)
# model.load_state_dict(ckpt['model_dict'])
# torch.onnx.export(model, dummy_input, onnx_model_path, verbose=True)

image = cv2.imread('test_imgs/5.jpg')
net =  cv2.dnn.readNetFromONNX(onnx_model_path) 
blob = cv2.dnn.blobFromImage(image, 1.0 / 255, (224, 224),(0, 0, 0), swapRB=True, crop=False)
tic = time.time()
net.setInput(blob)
preds = net.forward()
print(time.time() - tic)
biggest_pred_index = np.array(preds)[0].argmax()
print ("Predicted class:", CLASSES[biggest_pred_index])
 


