# Importacao das bibliotecas
import cv2

# 1. Le a imagem com a funcao imread()
imagem = cv2.imread('imagens/messi5.jpg')

# 2. Converte a imagem para Escala de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # tente cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV

# 3. Mostra alguns atributos
print('Resolucao: ', imagem.shape)
print('Largura: ', imagem.shape[1])
print('Altura: ', imagem.shape[0])

# 4. Mostra a imagem na tela
cv2.imshow("Imagem", imagem) 
cv2.waitKey(0)     # aqui onde cria-se a janela e mostra-se a imagem