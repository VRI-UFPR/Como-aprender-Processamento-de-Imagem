# Importacao das bibliotecas
from matplotlib import pyplot as plt
import numpy as np
import cv2

# 1. Le a imagem e converte para escala de cinza
img = cv2.imread('imagens/wiki.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Faz a equalizacao do histograma a partir da Imagem
h_eq = cv2.equalizeHist(img)

# 3. Plota histograma original da imagem
plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])      # ravel transforma uma matrix em um vetor
plt.xlim([0, 256])
plt.show()

# 4. Plota histograma equalizado da imagem
plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

# 5. Mostra a imagem
#cv2.imwrite('saida2.jpg', h_eq)
cv2.waitKey(0)
