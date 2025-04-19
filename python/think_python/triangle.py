from turtle import *

def triangle():
    for _ in range(3):
        forward(100)
        left(120)

left(60)
for i in range(5):
    triangle()
    left(120 // 2) 

done()