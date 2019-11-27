from turtle import *
    

class Circulo:
    def __init__(self):
        self._desenho = Pen()
        self._desenho.shape('circle')
        self._desenho.shapesize(4)
        self._desenho.up()
        self._desenho.color('white')
        self._desenho.speed('fastest')

    def mover_cima(self):
        x = self._desenho.xcor()
        y = self._desenho.ycor() + 10
        self._desenho.goto(x, y)
        if self._desenho.ycor() > 250:
            y = -250
        self._desenho.goto(x, y)

    def mover_baixo(self):
        x = self._desenho.xcor()
        y = self._desenho.ycor() - 10
        self._desenho.goto(x, y)
        if self._desenho.ycor() < -250:
            y = 250
        self._desenho.goto(x, y)

    def mover_esquerda(self):
        x = self._desenho.xcor() - 10
        y = self._desenho.ycor() 
        self._desenho.goto(x, y)
        if self._desenho.xcor() < -400:
            x = 400
        self._desenho.goto(x, y)

    def mover_direita(self):
        x = self._desenho.xcor() + 10
        y = self._desenho.ycor() 
        if self._desenho.xcor() > 400:
            x = -400
        self._desenho.goto(x, y)



def main():
    tela = Screen()
    tela.setup(800, 500)
    tela.bgcolor('black')

    circulo = Circulo()


    tela.listen()
    tela.onkey(circulo.mover_direita, 'Right')
    tela.onkey(circulo.mover_esquerda, 'Left')
    tela.onkey(circulo.mover_cima, 'Up')
    tela.onkey(circulo.mover_baixo, 'Down')

    done()



if __name__ == '__main__':
    main()