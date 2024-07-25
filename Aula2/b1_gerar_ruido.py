# https://stackoverflow.com/questions/14435632/impulse-gaussian-and-salt-and-pepper-noise-with-opencv

# =============================================================================
#  Header
# =============================================================================

import cv2
import numpy as np

# =============================================================================
#  Funcoes
# =============================================================================

def add_salt_and_pepper(imagem, prob):
    """
    Adiciona ruido tipo sal e pimenta para a imagem

    imagem: imagem de um canal de 0 a 255
    prob: probabilidade (limiar) do ruido

    Exemplo: 
        imagem = cv2.imread("imagens/casa.jpg")
        imagem_ruidosa = add_salt_and_pepper(imagem, 0.05)
    """
    
    mat_aleatoria = np.random.rand(imagem.shape[0], imagem.shape[1])
    ruidosa = imagem.copy()
    ruidosa[ mat_aleatoria < prob ] = 0
    ruidosa[ mat_aleatoria > 1.0 - prob ] = 255
    return ruidosa

def add_gaussian_noise(image, sigma):
    """
        Adiciona ruido tipo gaussiana para a imagem

        imagem: imagem de um canal de 0 a 255
        sigma: fator de multiplicacao do ruido

        Exemplo: 
            imagem = cv2.imread("imagens/casa.jpg")
            imagem_ruidosa = add_gaussian_noise(imagem, 10.0)
    """

    img = np.array(image)
    noise = np.random.randn(img.shape[0], img.shape[1], img.shape[2])
    img = img.astype('int16')
    img_noise = img + noise * sigma
    img_noise = np.clip(img_noise, 0, 255)
    img_noise = img_noise.astype('uint8')
    return img_noise


# =============================================================================
#  Main
# =============================================================================

imagem = cv2.imread("messi.jpg")
# imagem = add_salt_and_pepper(imagem, 0.25)
imagem = add_gaussian_noise(imagem, 25.0)
cv2.imwrite("imagens3/messi.jpg", imagem)
