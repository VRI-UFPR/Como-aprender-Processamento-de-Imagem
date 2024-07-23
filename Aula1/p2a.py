# Importacao das bibliotecas
import cv2
import numpy as np

# 1. Le a imagem
image = cv2.imread('imagens/messi5.jpg')

# 2. Corta um pedaco da imagem e mostra a imagem
(b, g, r) = image[10, 10]
print('O pixel (10, 10) tem os valores nos canais:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
cv2.imshow("imagem", image)
cv2.waitKey(0)

# 3. Constantes para convertScaleAbs
alpha = 1.0
beta = 240

# 3.1: usando a funcao convertScaleAbs
new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# 3.1: mostra a imagem e o valor do pixel na coordenada 10,10
(b, g, r) = new_image[10, 10]
print('\nO pixel (10, 10) tem os valores nos canais:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
cv2.imshow("imagem", new_image)
cv2.waitKey(0)

# 3.2: fazendo manualmente
new_image = np.zeros(image.shape, image.dtype)
for y in range(0, image.shape[0]):
  for x in range(0, image.shape[1]):
    new_image[y, x] = np.clip(alpha * image[y,x] + beta, 0 , 255)

# 3.2: mostra a imagem e o valor do pixel na coordenada 10,10 
(b, g, r) = new_image[10, 10]
print('\nO pixel (10, 10) tem os valores nos canais:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
cv2.imshow("imagem 1", new_image)
cv2.waitKey(0)