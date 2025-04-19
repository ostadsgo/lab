from turtle import *

def triangle():
    for _ in range(3):
        forward(100)
        left(120)

left(30)
for i in range(6):
    triangle()
    left(60) 

done()