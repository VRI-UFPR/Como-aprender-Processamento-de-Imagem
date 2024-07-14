# Importacao das bibliotecas
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. Le a imagem e converte para escala de cinza
img = cv2.imread('images/wiki.jpg',0)
cv2.imshow("Imagem original", img)
cv2.waitKey(0)

# 
hist,bins = np.histogram(img.flatten(),256,[0,256])

# 
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

# Plota 
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('Somatorio','histograma'), loc = 'upper left')
plt.show()

#
h_eq = cv2.equalizeHist(img)
cv2.imshow("Imagem Equalizada", h_eq)
cv2.waitKey(0)

# 
hist2,bins2 = np.histogram(h_eq.flatten(),256,[0,256])

#
cdf2 = hist2.cumsum()
cdf2_normalized = cdf2 * hist2.max()/ cdf2.max()

# Plota 
plt.plot(cdf2_normalized, color = 'b')
plt.hist(h_eq.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('Somatorio','histograma'), loc = 'upper left')
plt.show()




