# Importacao das bibliotecas
import cv2

# 1. Le a imagem com a funcao imread()
imagem = cv2.imread('imagens/messi5.jpg')

# 2. Mostra alguns atributos
print(imagem.shape)
print('Largura: ', imagem.shape[1])
print('Altura: ', imagem.shape[0])
print('Canais de Cor: ', imagem.shape[2])

# 3. Mostra a imagem na tela
cv2.imshow("Imagem Colorida", imagem) 
cv2.waitKey(0)     # aqui onde cria-se a janela e mostra-se a imagem

# 4. Salvar a imagem para um arquivo no formato JPG
cv2.imwrite("saida.jpg", imagem)