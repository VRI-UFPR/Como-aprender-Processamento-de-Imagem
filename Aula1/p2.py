# Importacao das bibliotecas
import cv2
import numpy as np

# 1. Le a imagem
image = cv2.imread('imagens/messi5.jpg')

# 2. Corta um pedaco da imagem
(b, g, r) = image[10, 10]
print('O pixel (10, 10) tem os valores nos canais:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

# 3. Mostra a imagem
cv2.imshow("Imagem original", image)
cv2.waitKey(0)


# 4. cv2.convertScaleAbs

alpha = 1.0
beta = 130

# Opcao 1:
#new_image = np.zeros(image.shape, image.dtype)
#for y in range(0, image.shape[0]):
#  for x in range(0, image.shape[1]):
#    new_image[y, x] = np.clip(alpha * image[y,x] + beta, 0 , 255)

# Opcao 2:
new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
(b, g, r) = new_image[10, 10]
print('\nO pixel (10, 10) tem os valores nos canais:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

# 5. 
cv2.imshow("Imagem modificada", new_image)
cv2.waitKey(0)

