# Exercício 2: 
# 
# Faca um script usando OpenCV que leia todas as imagens JPG da pasta Aula1/imagens e 
# redimensione todas elas para 640x480 e em escala de cinza. E salve cada imagem 
# na pasta saida/
#
# Consulte a documentação do OpenCV para saber quais funções 
# utilizar: https://docs.opencv.org/4.x/d7/d16/tutorial_py_table_of_contents_core.html
# 
# * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Importacao das bibliotecas
import cv2
import numpy as np
import glob
from pathlib import Path

# 1. Para cada arquivo JPG na pasta imagens
for file in glob.glob("imagens/*.jpg"):
    name = Path(file).name
    print(file, " --- ", name)