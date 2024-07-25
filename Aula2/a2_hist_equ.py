# Importacao das bibliotecas
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. Le a imagem e converte para escala de cinza
imagem = cv2.imread('imagens/casa.jpg',0)
cv2.imshow("Imagem original", imagem)
cv2.waitKey(0)

# 2. Mostra os dados da imagem original

# 2.1. Calcula o histograma usando a biblioteca Numpy
hist,bins = np.histogram(imagem.flatten(), 256, [0,256])
# print(hist)

# 2.2. Calcula o Cumulative Distribution Function (CDF)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()
# print(cdf)
# print(cdf_normalized)

# 2.3. Plota 
plt.plot(cdf_normalized, color = 'b')
plt.hist(imagem.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('Somatorio','histograma'), loc = 'upper left')
plt.show()


# 3. Equaliza uma imagem atraves da Equalização do Histograma
equalizada = cv2.equalizeHist(imagem)
cv2.imshow("Imagem Equalizada", equalizada)
cv2.waitKey(0)


# 4. Mostra os dados da imagem equalizada

# 4.1. Calcula o Cumulative Distribution Function (CDF)
hist2,bins2 = np.histogram(equalizada.flatten(),256,[0,256])
cdf2 = hist2.cumsum()
cdf2_normalized = cdf2 * hist2.max()/ cdf2.max()

# 4.2. Plota o grafico
plt.plot(cdf2_normalized, color = 'b')
plt.hist(equalizada.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('Somatorio','histograma'), loc = 'upper left')
plt.show()




