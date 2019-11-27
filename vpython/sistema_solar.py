from vpython import *
from math import sqrt, sin, cos, pi


raio = 60

a, b, c = 0, 0, 1
teta = (pi*45)/180
matriz_rotacao = {
    1: cos(teta)+(1-cos(teta)*a**2),
    2: (1-cos(teta))*a*b + sin(teta)*c,
    3: (1 - cos(teta))*a*c - sin(teta)*b,
    4: (1 - cos(teta))*b*a - sin(teta)*c,
    5: cos(teta) + (1 - cos(teta))*b**2,
    6: (1 - cos(teta))*b*c + sin(teta)*a,
    7: (1 - cos(teta))*c*a + sin(teta)*b,
    8: (1 - cos(teta))*c*b - sin(teta)*a,
    9: cos(teta) + (1 - cos(teta))*c**2,
}


class Estrela:
    def __init__(self, tamanho:float, cor):
        self._desenho = sphere(pos=vector(0,0,0), radius=tamanho, color=cor)
        self._raios = [
            arrow(pos=vector(0,0,0), axis=vector(0,40,0), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(40,0,0), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(0,0,40), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(0,-40,0), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(-40,0,0), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(0,0,-40), color=cor),
            
            arrow(pos=vector(0,0,0), axis=vector(40/sqrt(2), 40/sqrt(2), 0), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(-40/sqrt(2), 40/sqrt(2), 0), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(40/sqrt(2), -40/sqrt(2), 0), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(-40/sqrt(2), -40/sqrt(2), 0), color=cor),

            arrow(pos=vector(0,0,0), axis=vector(40/sqrt(2), 0, 40/sqrt(2)), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(-40/sqrt(2), 0, 40/sqrt(2)), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(40/sqrt(2), 0, -40/sqrt(2)), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(-40/sqrt(2), 0, -40/sqrt(2)), color=cor),

            arrow(pos=vector(0,0,0), axis=vector(0, 40/sqrt(2), 40/sqrt(2)), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(0, -40/sqrt(2), 40/sqrt(2)), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(0, 40/sqrt(2), -40/sqrt(2)), color=cor),
            arrow(pos=vector(0,0,0), axis=vector(0, -40/sqrt(2), -40/sqrt(2)), color=cor),
        ]



class Planeta:
    def __init__(self, tamanho:float, cor, posicao_sistema:int):
        self._desenho = sphere(pos=vector(0,0,0), radius=tamanho, color=cor)
        self._posicao_sistema = posicao_sistema

    def translacao(self, angulo):
        if self._posicao_sistema != 9:
            angulo *= 10 - self._posicao_sistema
            
            a = self._posicao_sistema * raio
            b = a/2
            
            r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)
            
            x = r*cos(pi*angulo/180)
            y = 0
            z = r*sin(pi*angulo/180)

            self._desenho.pos = vector(x, y, z)

        else:
            angulo *= (10 - self._posicao_sistema)
            a = self._posicao_sistema * raio
            b = a/2
            
            r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)
            
            x = r*cos(pi*angulo/180)
            y = 0
            z = r*sin(pi*angulo/180)
            
            x1 = x*matriz_rotacao[1] + y*matriz_rotacao[2] + z*matriz_rotacao[3]
            y1 = x*matriz_rotacao[4] + y*matriz_rotacao[5] + z*matriz_rotacao[6]
            z1 = x*matriz_rotacao[7] + y*matriz_rotacao[8] + z*matriz_rotacao[9]
            
            self._desenho.pos = vector(x1, y1, z1)

            

def main():

    try:
        sol = Estrela(30, vector(255/255, 255/255, 0))

        mercurio = Planeta(3, vector(128/255, 128/255, 128/255), 1)
        venus = Planeta(5, vector(255/255, 140/255, 0), 2)
        terra = Planeta(6, vector(0, 0, 255/255), 3)
        marte = Planeta(4, vector(255/255, 0, 0), 4)
        jupiter = Planeta(10, vector(244/255, 164/255, 96/255), 5)
        saturno = Planeta(9, vector(218/255, 165/255, 32/255), 6)
        urano = Planeta(8, vector(60/255, 179/255, 113/255), 7)
        netuno = Planeta(7, vector(70/255, 130/255, 180/255), 8)
        plutao = Planeta(2, vector(255/255, 218/255, 185/255), 9)
        


        angulo = 0
        while True:
            mercurio.translacao(angulo)
            venus.translacao(angulo)
            terra.translacao(angulo)
            marte.translacao(angulo)
            jupiter.translacao(angulo)
            saturno.translacao(angulo)
            urano.translacao(angulo)
            netuno.translacao(angulo)
            plutao.translacao(angulo)
            
            angulo = (angulo+1) % 360

            rate(20)
    except: pass

if __name__ == '__main__':
    main()