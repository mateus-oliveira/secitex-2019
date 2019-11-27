'''
Hexaedro
'''

# VPython
from vpython import *

# Coordenadas para os vértices e arestas
coords = (-3, 3)

# Cor do vértice
cor1 = vector(0.9, 0.9, 1.0)

# Cor da aresta
cor2 = vector(0.5, 0.5, 0.6)

# Desenha esferas nos vértices

for x in coords:
    for y in coords:
        for z in coords:

            # pops e a posição do centro da esfera
            sphere(pos=vector(x, y, z))


# Desenha os cilindros das arestas
for x in coords:
    for z in coords:

        # pos é a posição do centro da base do cilindro
        # radius é o raio da base do cilindro
        # axis é o eixo do cilindro
        cylinder(pos=vector(x, 3, z), 
                 radius=0.25, axis=vector(0, -6, 0))

    for y in coords:
        cylinder(pos=vector(x, y, 3), 
                 radius=0.25, axis=vector(0, 0, -6))

for y in coords:
    for z in coords:
        cylinder(pos=vector(3, y, z), 
                radius=0.25, axis=vector(-6, 0, 0))
