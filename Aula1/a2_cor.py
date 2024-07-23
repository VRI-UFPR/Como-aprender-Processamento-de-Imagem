# Importacao das bibliotecas
import cv2
import numpy as np

# 1. Le a imagem com a funcao imread()
imagem = cv2.imread('imagens/opencv_logo.png')

# 2. Separa os canais de cor
canal_b = imagem[:, :, 0]
canal_g = imagem[:, :, 1]
canal_r = imagem[:, :, 2]

# 3. Mostra os canais de cor separadamente
cv2.imshow("Imagem", canal_r) 
cv2.waitKey(0)
cv2.imshow("Imagem", canal_g) 
cv2.waitKey(0)
cv2.imshow("Imagem", canal_b) 
cv2.waitKey(0)

# 4. Junta diferentes canais de cores
zeros = np.zeros(imagem.shape[:2], dtype = "uint8")
imagem_azul_vermelho = cv2.merge([canal_b, zeros, canal_r])
cv2.imshow("Imagem", imagem_azul_vermelho) 
cv2.waitKey(0)

# 5. Converte a imagem para Escala de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # tente cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV
print('Resolucao: ', imagem.shape)
print('Largura: ', imagem.shape[1])
print('Altura: ', imagem.shape[0])
cv2.imshow("Imagem", imagem) 
cv2.waitKey(0)
