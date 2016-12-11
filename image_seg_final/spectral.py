import numpy as np
import cv2
import matplotlib.pyplot as plt

from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

def getLikelihood(imageFile,n):
	img = cv2.imread(imageFile)
	mask = img.astype(bool)
	
	img = img.astype(float)
	img += 1 + 0.2 * np.random.randn(*img.shape)

	graph = image.img_to_graph(img, mask=mask)
	graph.data = np.exp(-graph.data / graph.data.std())	

	labels = spectral_clustering(graph, n_clusters=3, eigen_solver='arpack')
	label_im = -np.ones(mask.shape)
	label_im[mask] = labels

	#plt.matshow(img)
	#plt.matshow(label_im)

	return label_im,len(label_im)

def getData(image,n):
	f = open('spectralData.txt', 'w')
	dataList,dataSize = getLikelihood(image,n)
	for data in range(0,dataSize):
		f.write(str(dataList[data])+"\n")
	f.close()

getData("half_box.jpg",2)
