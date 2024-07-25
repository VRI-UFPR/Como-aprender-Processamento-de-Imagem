# Exercício 1
#
# Faca um script em python que:
#  1. abra a imagem casa.jpg no formato colorido
#  2. seta o valor 0 para valores abaixo de 100 no canal azul
#  3. mostre o histograma e a imagem colorida com o canal azul alterado
#
# Consulte a documentação do OpenCV para saber como separar os canais da imagem: 
# https://docs.opencv.org/4.x/d7/d16/tutorial_py_table_of_contents_core.html
# 
# * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Importacao das bibliotecas
import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = "imagens/casa.jpg"
