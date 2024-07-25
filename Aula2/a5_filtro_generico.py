# Importacao das bibliotecas
import numpy as np
import cv2

# 1. le a imagem
imagem = cv2.imread('imagens/casa.jpg', 0)

# 2. Nucleo do filtro do Blur
nucleo = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

# outra forma de escrita:
#   nucleo = np.ones((3, 3), np.float32) / 9

# 3. passa o nucleo do filtro por toda a imagem
borrada = cv2.filter2D(imagem, -1, nucleo)
# print(borrada.dtype)

# 4. mostra a imagem
cv2.imshow("imagem", borrada)
cv2.waitKey(0)