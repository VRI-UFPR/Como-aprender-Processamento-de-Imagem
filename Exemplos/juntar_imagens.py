import cv2
import numpy as np

# Carregar as imagens
image1 = cv2.imread('imagens/esquerda.png')
image2 = cv2.imread('imagens/direita.png')

# Converter as imagens para tons de cinza
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Inicializar o detector SIFT
sift = cv2.SIFT_create()

# Encontrar pontos chave e descritores nas duas imagens
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# Emparelhamento dos pontos chave usando FLANN
matcher = cv2.FlannBasedMatcher()
matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

# Filtrar correspondências usando o teste de razão de Lowe
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# Desenhar correspondências
matched_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Mostrar a imagem combinada
cv2.imshow('Matches', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()