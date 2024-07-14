from matplotlib import pyplot as plt

import cv2

img = cv2.imread('images/home.jpg')
cv2.imshow("Original", img)

(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Original", img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)

b = cv2.calcHist([canalAzul], [0], None, [256], [0, 256])
g = cv2.calcHist([canalVerde], [0], None, [256], [0, 256])
r = cv2.calcHist([canalVermelho], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(b,"b")
plt.plot(g,"g")
plt.plot(r,"r")
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
