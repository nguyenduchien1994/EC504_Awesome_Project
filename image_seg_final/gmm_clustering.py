from __future__ import division
import numpy as np
import cv2
from sklearn.cluster import KMeans
from scipy.spatial import distance
imageFile = "/home/aditya/image_seg_final/plane.jpg"
img = cv2.imread(imageFile)
#print img.shape
newimg = img.reshape(-1,3)

#print newimg
#print type(newimg)

import time
import itertools

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn import mixture

# Fit a mixture of Gaussians with EM using two components
gmm = mixture.GMM(n_components=3, covariance_type='diag')

t0 = time.time()

gmm.fit(newimg)

t1 = time.time()

y_pred = gmm.predict(newimg)

a = gmm.predict_proba(newimg)
print a
#print gmm.score_samples(newimg)

print y_pred

import csv
with open ("gmmoutput.txt", "w") as f:
    for data in range(0,len(a)):
        f.write(str(round(a[data][0]*10))+"\n")
        #f.write(str(round(a[data][0]*10))+" "+str(round(a[data][1]*10))+" "+str(round(a[data][2]*10))+"\n")
f.close()
