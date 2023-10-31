import numpy as np
import matplotlib.pyplot as plt

def obter_coordenadas(tipo, numero_camera):
    print(f"Digite os Dados da {tipo} {numero_camera}")
    x = float(input(f"Digite a coordenada x da {tipo} {numero_camera}: "))
    y = float(input(f"Digite a coordenada y da {tipo} {numero_camera}: "))
    return x, y

def calcular_intersecao(x1, y1, x2, y2):
    xi = (x1 + x2) / 2
    yi = (y1 + y2) / 2
    return xi, yi

# Obter coordenadas da Camera 1 e Projeção 1
xc1, yc1 = obter_coordenadas("Camera", 1)
xp1, yp1 = obter_coordenadas("Projeção da Camera", 1)

# Obter coordenadas da Camera 2 e Projeção 2
xc2, yc2 = obter_coordenadas("Camera", 2)
xp2, yp2 = obter_coordenadas("Projeção da Camera", 2)

# Calcular a interseção das retas
xi, yi = calcular_intersecao(xc1, yc1, xc2, yc2)

# Exibir resultados
print(f"xi = {xi}")
print(f"yi = {yi}")

# Criar gráfico
x = np.linspace(0, 3, 100)
y1 = np.linspace(yc1, yp1, 100)
y2 = np.linspace(yc2, yp2, 100)

plt.plot(x, y1, label='Projeção da Camera 1')
plt.plot(x, y2, label='Projeção da Camera 2')
plt.scatter(xi, yi, color='green', label='Posição do Objeto')
plt.scatter(xc1, yc1, color='red', label='Camera 1')
plt.scatter(xc2, yc2, color='purple', label='Camera 2')

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title("Cruzamento de Retas")
plt.legend()
plt.show()
