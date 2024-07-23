# Importacao das bibliotecas
from matplotlib import pyplot as plt
import cv2

# 1. Le a imagem
imagem = cv2.imread('imagens/messi5.jpg')

# 2. Converte  a imagem de BGR para Escala de Cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)   #converte P&B
cv2.imshow("Imagem P&B", imagem)
cv2.waitKey(0)

# 3. Calcula o Histograma da imagem
h = cv2.calcHist([imagem], [0], None, [256], [0, 256])

# 4. Plota o histograma da imagem
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
# plt.hist(imagem.ravel(),256,[0,256])
plt.show()

# 5. Mostra a imagem e espera uma tecla
cv2.waitKey(0)