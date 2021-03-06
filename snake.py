"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import random

#Te da un numero aleatorio para x y y
#en el rango del tamanio de la pantalla 
#con un paso de 10 y lo coloca en los
#valores iniciales


firstX = randrange(-190, 190, 10)
firstY = randrange(-190, 190, 10)
food = vector(firstX, firstY)
snake = [vector(10, 0)]
aim = vector(0, -10)



def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9,a)

    square(food.x, food.y, 9,b) #SE RECIBEN LOS COLORES
    update()
    ontimer(move, 100)


colorsSnake = ['green','blue','yellow','black','purple']
colorsFood = ['yellow','black','purple','green','blue'] #COLORES DISPONIBLES
a = random.choice(colorsFood) #ELECCIÓN RANDOM
b = random.choice(colorsSnake)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
