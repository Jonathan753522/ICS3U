#Part 1
import turtle

t = turtle.Turtle()


for i in range(4):
    t.forward(100)
    t.left(90)

#Part 2
import turtle

t = turtle.Turtle()

for i in range(60):
  t.forward(100)
  t.left(63)

#Part 3
import turtle

t = turtle.Turtle()

t.goto(100, 100)

t.pendown()
t.penup()

t.dot(20, "red")
