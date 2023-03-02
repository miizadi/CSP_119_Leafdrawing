import turtle as trtl
import random 
painter = trtl.Turtle()
def tri():
  for i in range(3):
      if random_shape1 == "triangle":
        painter.forward(random_size1)
        painter.right(120)
sets = int(input("Do you want to draw the leaf? [press 1 to start]: "))
leaf_shape1 = ["circle", "triangle"]
leaf_size1 = [100, 50]
leaf_color1 = ["red", "green"]
random_shape1 = random.choice(leaf_shape1)
random_size1 = random.choice(leaf_size1)
random_color1 = random.choice(leaf_color1)

if sets == 1:
  painter.penup()
  painter.goto(-100,-100)
  painter.pendown()
  painter.left(90)
  painter.forward(50)
if  random_shape1 == "triangle":
  for i in range(3):
    painter.begin_fill()
    painter.color(random_color1)
    tri()
    painter.end_fill()
    painter.left(90)
if random_shape1 == "triangle":
  painter.right(45)
  painter.forward(100)
for i in range(2):
  if random_shape1 == "circle":
    painter.begin_fill()
    painter.color(random_color1)
    painter.circle(random_size1)
    painter.end_fill()
    painter.right(180)
if random_shape1 == "circle":
  painter.forward(50)
  painter.right(90)
  painter.begin_fill()
  painter.color(random_color1)
  painter.circle(random_size1)
  painter.end_fill()

wn = trtl.Screen()
wn. mainloop()
