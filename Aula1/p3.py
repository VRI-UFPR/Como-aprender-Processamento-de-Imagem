# Importacao das bibliotecas
from matplotlib import pyplot as plt
import cv2

# 1. Lee a imagem
img = cv2.imread('imagens/messi5.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #converte P&B

# 2. Mostra a imagem
cv2.imshow("Imagem P&B", img)
cv2.waitKey(0)

# 3. Calcula o Histograma da imagem
h = cv2.calcHist([img], [0], None, [256], [0, 256])

# 4. Plota o histograma da imagem
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
# plt.hist(img.ravel(),256,[0,256])
plt.show()

# 5. Mostra a imagem e espera uma tecla
cv2.waitKey(0)