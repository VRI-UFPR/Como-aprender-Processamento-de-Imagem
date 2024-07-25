# Importacao das bibliotecas
import cv2
import numpy as np

# 1. le a imagem
imagem = cv2.imread('imagens/casa.jpg', 0)

# 2. executa o filtro canny
bordas = cv2.Canny(imagem, 100, 200)

# 3. mostra a imagem
cv2.imshow("imagem", bordas)
cv2.waitKey(0)