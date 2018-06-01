import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("black")



	spiral = turtle.Turtle()
	spiral.shape("turtle")
	spiral.color("white")
	for i in range(40):
		spiral.forward(i * 10)
		spiral.right(144)

	# sara = turtle.Turtle()
	# sara.shape("arrow")
	# sara.color("white")
	# sara.speed(3)
	# for i in range (0, 36):
	# 	count=0
	# 	while count<4:
	# 		sara.forward(100)
	# 		sara.right(90)
	# 		count+=1
	# 	sara.right(10)

	# besho = turtle.Turtle()
	# besho.shape("arrow")
	# besho.color("red")
	# besho.circle(100)

	# baby = turtle.Turtle()
	# baby.shape("arrow")
	# baby.color("green")
	# baby.forward(100) 
	# baby.right(120)
	# baby.forward(100)
	# baby.right(120)
	# baby.forward(100)

	window.exitonclick()

draw_square()