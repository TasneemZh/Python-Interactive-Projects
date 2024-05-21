from turtle import Turtle, Screen

screen = Screen()
bob = Turtle()


def go_forward():
    bob.forward(10)


def go_backward():
    bob.backward(10)


def go_counter_clockwise():
    bob.setheading(bob.heading() + 10)


def go_clockwise():
    bob.setheading(bob.heading() - 10)


def clear_screen():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()


screen.listen()
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="a", fun=go_counter_clockwise)
screen.onkey(key="d", fun=go_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
