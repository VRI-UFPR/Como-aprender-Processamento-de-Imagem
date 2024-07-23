# Importacao das bibliotecas
import cv2
import numpy as np

# 1. Leitura da Imagem
img = cv2.imread('imagens/messi5.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

# 2. Cria uma imagem zerada de mesmo tamanho 
zeros = np.zeros(img.shape[:2], dtype = "uint8")

# 3. Cria uma imagem BGR com apenas os valores de vermelho
bgr_vermelho = cv2.merge([zeros, zeros, canalVermelho])
cv2.imshow("Vermelho", bgr_vermelho)
cv2.waitKey(0)

# 4. Cria uma imagem BGR com apenas os valores de verde
bgr_verde = cv2.merge([zeros, canalVerde, zeros])
cv2.imshow("Verde", bgr_verde)
cv2.waitKey(0)

# 5. Cria uma imagem BGR com apenas os valores de azul
bgr_azul = cv2.merge([canalAzul, zeros, zeros])
cv2.imshow("Azul", bgr_azul)
cv2.waitKey(0)

# 6. Mostra a imagem original juntando todos os canais de cores
bgr_original = cv2.merge([canalAzul, canalVerde, canalVermelho])
cv2.imshow("Original", bgr_original)

# 7. Espera o usuario apertar uma tecla
cv2.waitKey(0)
