import turtle


tom = turtle.Turtle()
screen = turtle.Screen()
screen.listen()
tom.shape('turtle')
tom.color('beige')
tom.pencolor('lime')
screen.bgcolor('black')
tom.speed('fastest')
def move_forward():
   tom.forward(10)
screen.onkey(move_forward,'w')

def move_backwards():
    tom.backward(10)
screen.onkey(move_backwards,'s')

def move_left():
    tom.left(10)
    tom.forward(10)
screen.onkey(move_left,'a')

def move_right():
    tom.right(10)
    tom.forward(10)
screen.onkey(move_right,'d')

def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.onkey(clear_screen,'c')


screen.exitonclick()
