# Importacao das bibliotecas
import numpy as np
import cv2

# 1. Le a imagem em escala de cinza
imagem = cv2.imread('imagens/casa.jpg', 0)

imagem = cv2.GaussianBlur(imagem, (5,5), 0)
imagem = cv2.GaussianBlur(imagem, (5,5), 0)

# 2. Passa o filtro Sobel no eixo X
sobel_x_f64 = cv2.Sobel(imagem, cv2.CV_64F, 1, 0)
sobel_x_f64_positive = np.absolute(sobel_x_f64)
sobel_x_u8_positive = np.uint8(sobel_x_f64_positive)

# 3. Passa o filtro Sobel no eixo Y
sobel_y_f64 = cv2.Sobel(imagem, cv2.CV_64F, 0, 1)
sobel_y_f64_positive = np.absolute(sobel_y_f64)
sobel_y_u8_positive = np.uint8(sobel_x_f64_positive)

# 4. Junta as duas imagens atraves da operacao Or bit a bit
sobel_xy_u8_positive = cv2.bitwise_or(sobel_x_u8_positive, sobel_y_u8_positive)

# 4. Concatena as imagens
resultado = np.vstack([
    np.hstack([imagem, sobel_x_u8_positive]),
    np.hstack([sobel_y_u8_positive, sobel_xy_u8_positive])
])

# Mostra o resultado concatenado
cv2.imshow("Sobel", resultado)
cv2.waitKey(0)
