# Exercício 2
#
# 
#
# Consulte a documentação do OpenCV para saber como separar os canais da imagem: 
# https://docs.opencv.org/4.x/d7/d16/tutorial_py_table_of_contents_core.html
# 
# * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Importacao das bibliotecas
import cv2
import numpy as np

# 1. le a imagem
imagem = cv2.imread('imagens/casa.jpg', 0)

# 2. executa o laplaciano e converte em escala absoluta
laplaciano = cv2.Laplacian(imagem, cv2.CV_32F)
laplaciano_abs = cv2.convertScaleAbs(laplaciano)

# 3. mostra a imagem
cv2.imshow("imagem", laplaciano_abs)
cv2.waitKey(0)