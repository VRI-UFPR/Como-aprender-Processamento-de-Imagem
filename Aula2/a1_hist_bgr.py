# Importacao das bibliotecas
import cv2
from matplotlib import pyplot as plt

# 1. Leitura da Imagem
imagem = cv2.imread('imagens/casa.jpg')
cv2.imshow("Original", imagem)

# 2. Divide cada canal da imagem BGR para uma imagem separadamente
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)
  # o mesmo que:
  #   canalAzul = imagem[:, :, 0]
  #   canalVerde = imagem[:, :, 1]
  #   canalVermelho = imagem[:, :, 2]

cv2.imshow("Original", imagem)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)

# 3. Calcula o Histograma de cada Imagem
#  - lembrando que: cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
azul = cv2.calcHist([canalAzul], [0], None, [256], [0, 256])
verde = cv2.calcHist([canalVerde], [0], None, [256], [0, 256])
vermelho = cv2.calcHist([canalVermelho], [0], None, [256], [0, 256])

# 4. Plota os histogramas
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(azul,"b")
plt.plot(verde,"g")
plt.plot(vermelho,"r")
plt.xlim([0, 256])
plt.show()

# 5. Espera o usuario apertar uma tecla
cv2.waitKey(0)
