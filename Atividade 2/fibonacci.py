# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math

def fibonacci_plot(n):
	previous_number = 0
	next_number = 1
	previous_square = previous_number
	next_square = next_number

	# Setting the colour of the plotting pen to blue
	pen.pencolor("blue")

	# Drawing the first square
	pen.forward(next_number*factor)
	pen.left(90)
	pen.forward(next_number*factor)
	pen.left(90)
	pen.forward(next_number*factor)
	pen.left(90)
	pen.forward(next_number*factor)

	# Proceeding in the Fibonacci Series
	temporary = next_square
	next_square = next_square+previous_square
	previous_square = temporary
	
	# Drawing the rest of the squares
	for i in range(1, n):
		pen.backward(previous_square*factor)
		pen.right(90)
		pen.forward(next_square*factor)
		pen.left(90)
		pen.forward(next_square*factor)
		pen.left(90)
		pen.forward(next_square*factor)

		# Proceeding in the Fibonacci Series
		temporary = next_square
		next_square = next_square+previous_square
		previous_square = temporary

	# Bringing the pen to starting point of the spiral plot
	pen.penup()
	pen.setposition(factor, 0)
	pen.seth(0)
	pen.pendown()

	# Setting the colour of the plotting pen to blue
	pen.pencolor("red")

	# Fibonacci Spiral Plot
	pen.left(90)
	for i in range(n):
		print(next_number)
		spiral_line = (math.pi
					* next_number
					* factor/2)
		spiral_line /= 90
		for j in range(90):
			pen.forward(spiral_line)
			pen.left(1)
		temporary = previous_number
		previous_number = next_number
		next_number = temporary+next_number


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Taking Input for the number of
# Iterations our Algorithm will run
interations = int(input
				('Enter the number of iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if interations>0:
	print("Fibonacci series for", interations, "elements :")

	pen = turtle.Turtle()
	pen.speed(1)

	fibonacci_plot(interations)

	turtle.done()
else:
	print("Number of iterations must be > 0")