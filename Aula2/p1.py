# Importacao das bibliotecas
import cv2

# 1. Leitura da Imagem
img = cv2.imread('images/messi5.jpg')
cv2.imshow("Original", img)

# 2. Conversao da Imagem BGR para Escala de Cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# 3. Conversao da Imagem BGR para o formato HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# 4. Conversao da Imagem BGR para o formato LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

# 5. Mostra todas as imagens e espera o usuario apertar uma tecla
cv2.waitKey(0)
