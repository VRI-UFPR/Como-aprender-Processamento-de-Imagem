# Importacao das bibliotecas
import cv2
import numpy as np

# Le a imagem
original = cv2.imread('imagens/casa.jpg',0)
cv2.imshow("Original", original)
cv2.waitKey(0)

# Aplica um filtro Gaussiana com kernel 3x3
borrada = cv2.GaussianBlur(original, (3,3), 0)
cv2.imshow("Gaussian 3x3", borrada)
cv2.waitKey(0)

# Aplica um filtro Gaussiana com kernel 5x5
borrada = cv2.GaussianBlur(original, (5,5), 0)
cv2.imshow("Gaussian 5x5", borrada)
cv2.waitKey(0)

# Aplica um filtro mediana com kernel 3x3
borrada = cv2.medianBlur(original, 3)
cv2.imshow("Median 3x3", borrada)
cv2.waitKey(0)

# Aplica um filtro mediana com kernel 5x5
borrada = cv2.medianBlur(original, 5)
cv2.imshow("Median 5x5", borrada)
cv2.waitKey(0)

# Aplica um filtro normalized box com kernel 3x3
borrada = cv2.blur(original, (3,3))
cv2.imshow("Blur 3x3", borrada)
cv2.waitKey(0)

# Aplica um filtro normalized box com kernel 5x5
borrada = cv2.blur(original, (5,5))
cv2.imshow("Blur 5x5", borrada)
cv2.waitKey(0)