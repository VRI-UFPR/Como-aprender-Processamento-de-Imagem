# Importacao das bibliotecas
import cv2

# 1. Le a imagem com a funcao imread()
imagem = cv2.imread('imagens/messi5_gray.jpg')

# 2. Percorre a imagem incrementado o valor do Pixel
imagem2 = imagem.copy()
for y in range(0, imagem2.shape[0]):
  for x in range(0, imagem2.shape[1]):
    imagem2[y, x] = imagem2[y, x] + 50

cv2.imshow("Imagem", imagem2)
cv2.waitKey(0)

# 3. Incrementado parte de uma imagem por 100
parte = imagem[30:150,30:150]
parte += 100
cv2.imshow("Parte", parte)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)