from turtle import *
    

class Circulo:
    def __init__(self):
        self._desenho = Pen()
        self._desenho.shape('circle')
        self._desenho.shapesize(4)
        self._desenho.up()
        self._desenho.color('white')


    def mover_circulo(self):
        x, y = 0, 0  
        para_esquerda = False
        para_baixo = False
       
        while True:
            if x >= 400: 
                para_esquerda = True
            elif x <= -400: 
                para_esquerda = False

            if y >= 250:
                para_baixo = True 
            elif y <= -250:
                para_baixo = False

            
            if para_esquerda: x -= 1
            else: x += 1

            if para_baixo: y -= 1
            else: y += 1

            self._desenho.goto(x, y)


def main():
    try:
        tela = Screen()
        tela.setup(800, 500)
        tela.bgcolor('black')

        circulo = Circulo()
        circulo.mover_circulo()
    except:pass


if __name__ == '__main__':
    main()
