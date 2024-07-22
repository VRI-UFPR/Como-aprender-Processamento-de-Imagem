```
Como Aprender Processamento de Imagem
Copyright (C) 2024
  Lucas Ferrari
  Rayson Larocca
  Felipe Bombardelli

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

# Aula 1 - Introdução

Abrange métodos e operações para alterar, melhorar ou extrair informações de uma imagem digital.
Representação e Definições Básicas

Imagem Digital é uma matriz de dimensões LxC, onde cada célula corresponde a um pixel da imagem.

Pixel:

    A menor unidade de uma imagem digital. Em imagens em escala de cinza, cada pixel possui um valor que varia de 0 (preto) a 255 (branco). Em imagens RGB (Red, Green, Blue), cada pixel é composto por três valores, representando as intensidades das cores vermelha, verde e azul, cada uma variando de 0 a 255. A combinação dessas intensidades determina a cor final do pixel.

```python
# Carrega as bibliotecas necessárias
import cv2                       # OpenCV
import matplotlib.pyplot as plt  # Matplotlib
import numpy as np               # NumPy
from google.colab.patches import cv2_imshow # similar a cv2.imshow() do OpenCV
```

```bash
# Baixa uma imagem de exemplo da internet e salva-a com o nome 'astronaut.png'
!wget https://scikit-image.org/skimage-tutorials/_images/4_segmentation_15_0.png -O astronaut.png
```

```python
# Lê a imagem 'astronaut.png'
imagem = cv2.imread('astronaut.png')

# Configura o tamanho da figura para exibição
plt.figure(figsize=(6, 6))

# Exibe a imagem
plt.imshow(imagem)
plt.show()
```

![image](https://scikit-image.org/skimage-tutorials/_images/4_segmentation_15_0.png)


```python
# Converte a imagem de BGR para RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Configura o tamanho da figura para exibição
plt.figure(figsize=(6, 6))

# Exibe a imagem convertida (em RGB)
plt.imshow(imagem_rgb)
plt.show()
```

```python
# Obtém a altura, largura e número de canais da imagem
altura, largura, canais = imagem_rgb.shape

# O mesmo resultado da linha anterior poderia também ser alcançado da maneira abaixo:
# altura = imagem_rgb.shape[0]
# largura = imagem_rgb.shape[1]
# canais = imagem_rgb.shape[2]

# Imprime as dimensões da imagem
print(f'Dimensões da imagem:')
print(f'  Altura: {altura} pixels')
print(f'  Largura: {largura} pixels')
print(f'  Canais: {canais}')
```


## O que foi visto

- Leitura de imagem
- Mostrar e salvar uma imagem
- Cortar uma parte da imagem
- Converter uma imagem para diferentes representações (Escala Cinza, HUE, BGR)
- Calcula o histograma original e equalizado de uma imagem
- Plotar o histograma

Point operators
- Pixel transforms
- Color transforms
- Compositing and matting
- Histogram equalization
- Application: Tonal adjustment