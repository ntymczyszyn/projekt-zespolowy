from ultralytics import YOLO
import numpy as np
from IPython.display import Image, display
from IPython import display
import os

path =  os.path.join(os.path.dirname(__file__), "krasneleModel.pt")
model = YOLO(path)

krasneleresults = []

for j in range(0, 19):
    img_path = "krasnal" + str(j) + ".jpg"
    result = model(source=img_path, show=False, conf=0.3, save=True)
    for i, r in enumerate(result):

        im_bgr = r.plot()  
        r.show()
        r.save(filename=f'results\\results{j}{i}.jpg')
