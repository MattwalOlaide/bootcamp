import turtle

def draw_art():
  window = turtle.Screen()
  window.bgcolor("white")
  my_flower = turtle.Turtle()
  my_flower.shape("turtle")
  my_flower.color("red","yellow")
  my_flower.begin_fill()
  my_flower.speed(5)
  for i in range(0,36):
    my_flower.forward(100)
    my_flower.right(90)
    my_flower.forward(100)
    my_flower.left(90)
    my_flower.forward(100)
    my_flower.backward(90)
    my_flower.forward(100)
    my_flower.right(90)
    my_flower.right(10)
  my_flower.end_fill()
  my_flower.goto(0,180)
  

  window.exitonclick()

draw_art()