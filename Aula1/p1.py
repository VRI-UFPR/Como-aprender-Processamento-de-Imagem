# Importacao das bibliotecas
import cv2

# 1. Ler a imagem com a funcao imread()
imagem = cv2.imread('images/messi5_gray.jpg')

# 2. Mostra alguns atributos
print('Largura: ', imagem.shape[1])  # largura da imagem
print('Altura: ', imagem.shape[0])   # altura da imagem
print('Canais de Cor: ', imagem.shape[2])

# 3. Mostra a imagem na tela
cv2.imshow("Imagem Colorida", imagem) 
cv2.waitKey(0)     # aqui onde cria-se a janela e mostra-se a imagem

# 4. Salvar a imagem para um arquivo no formato JPG
cv2.imwrite("saida.jpg", imagem)




# Converte a imagem de BGR para Escala de Cinza
#imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
#print('Largura: ', imagem.shape[1]) #largura da imagem
#print('Altura: ', imagem.shape[0]) #altura da imagem
#print('Canais de Cor: ', imagem.shape[2])

#cv2.imshow("Imagem Gray", imagem)
#cv2.waitKey(0)

