# Importacao das bibliotecas
import cv2
import numpy as np

# 1. Leitura da Imagem
img = cv2.imread('messi5.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

#
zeros = np.zeros(img.shape[:2], dtype = "uint8")
cv2.imshow("Vermelho", cv2.merge([zeros, zeros,
canalVermelho]))

# Mostra as imagens
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
cv2.imshow("Original", img)

# 5. Espera o usuario apertar uma tecla
cv2.waitKey(0)
