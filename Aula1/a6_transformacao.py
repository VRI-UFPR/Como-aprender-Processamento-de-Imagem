# Importacao das bibliotecas
import cv2
import numpy as np

# 1. Le a imagem com a funcao imread()
imagem = cv2.imread('imagens/messi5.jpg')
cv2.imshow("imagem", imagem)
cv2.waitKey(0)

# 2. Espelha (flipa) a imagem horizontalmente
espelhada = cv2.flip(imagem, 1)
cv2.imshow("imagem", espelhada)
cv2.waitKey(0)


# 3. Espelha (flipa) a imagem horizontalmente

## 3.1. obtem o tamanho da imagem
altura_original = imagem.shape[0]
largura_original = imagem.shape[1]

## 3.2. calcula o novo tamanho da imagem
altura_nova = altura_original//2
largura_nova = largura_original

## 3.3. redimensiona a imagem
redimensionada = cv2.resize(imagem, (largura_nova, altura_nova))
cv2.imshow("imagem", redimensionada)
cv2.waitKey(0)


# 4. Concatena a imagem com ela mesma
concatenada = np.concatenate((imagem, imagem), axis=1)
cv2.imshow("imagem", redimensionada)
cv2.waitKey(0)

# 5. Rotaciona a imagem por 90, 180, 270 ou 360
rotacionada = cv2.rotate(imagem, cv2.ROTATE_90_CLOCKWISE)  # cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_90_COUNTERCLOCKWISE, ROTATE_180 
cv2.imshow("imagem", rotacionada)
cv2.waitKey(0)

# 6. Rotacionada por qualquer angulo

## 6.1. pega a constantes necessarias
altura = imagem.shape[0]
largura = imagem.shape[1]
centro_x = largura // 2
centro_y = altura // 2

## 6.2. calcula a matrix de rotacao para 45 graus
angulo = -30.0
matrix_rotacao = cv2.getRotationMatrix2D((20, 20), angulo, 1.0)
print(matrix_rotacao)

## 6.3. multiplica as matrix -> rotaciona a matrix em 45 graus
rotacionada = cv2.warpAffine(imagem, matrix_rotacao, (altura, largura))
cv2.imshow("imagem", rotacionada)
cv2.waitKey(0)

