# Exercício 3: 
# 
# Carregue uma imagem RGB messi5.jpg e converta-a para escala de cinza 
# sem usar as funcoes prontas da bibliotecas como OpenCV. Em seguida, compare o 
# resultado dessa conversão com a feita pela função cv2.cvtColor() do OpenCV.
#
# Dica: A conversão de um pixel colorido para um pixel em escala de cinza é feita 
# utilizando a seguinte fórmula:
#    Cinza = 0.2989 * Vermelho + 0.5870 * Verde + 0.1140 * Azul
# 
# * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Importacao das bibliotecas
import cv2
import numpy as np