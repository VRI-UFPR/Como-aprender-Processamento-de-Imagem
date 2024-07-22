# Importacao das bibliotecas
import cv2
from matplotlib import pyplot as plt

# 1. Leitura da Imagem
img = cv2.imread('images/home.jpg')
cv2.imshow("Original", img)

# 2. Divide cada canal da imagem BGR para uma imagem separadamente
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Original", img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)

# 3. Calcula o Histograma de cada Imagem
b = cv2.calcHist([canalAzul], [0], None, [256], [0, 256])
g = cv2.calcHist([canalVerde], [0], None, [256], [0, 256])
r = cv2.calcHist([canalVermelho], [0], None, [256], [0, 256])

# 4. Plota os histogramas
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(b,"b")
plt.plot(g,"g")
plt.plot(r,"r")
plt.xlim([0, 256])
plt.show()

# 5. Espera o usuario apertar uma tecla
cv2.waitKey(0)
