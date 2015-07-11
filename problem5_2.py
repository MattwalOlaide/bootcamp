import turtle
window = turtle.Screen()
window.bgcolor("brown")
my_flower = turtle.Turtle()
my_flower.shape("turtle")
my_flower.color("white")
def draw_my_object(sides):
	
	for i in range(0,(sides)):

		my_flower.forward(40)
		my_flower.right(65)
		
				

def num_my_object(sides,objects):
	
	for i in range(0,(objects)):
		my_flower.right(270)
		draw_my_object(sides)
		

	window.exitonclick()


num_my_object(5,3)
