from vpython import *

print(color.green)
'''
bola1 = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.green)
bola2 = sphere(pos=vector(-3,4,0), radius=0.5, color=color.red)

seta = arrow(pos=bola1.pos, axis=bola2.pos-bola1.pos, color=color.red)




r = vector(-3,4,0)

while r.x < 10:
    rate(10)
    #sphere(pos=r, radius=0.5, color=color.cyan)
    bola2.pos = r
    seta.axis = bola2.pos - bola1.pos
    r.x += 1

print('FIM')
'''

arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.yellow)
arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.white)
arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.blue)
bola = sphere(pos=vector(0,0,0), radius=0.2, color=color.red)
