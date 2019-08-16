# This program will be able to solve any quadratic equation, even if it doesn't have any real solutions.
# We will also aim to be able to solve quadratics with complex coefficients.
# We begin by importing the complex math module.
import cmath
from sys import exit

print """\
Welcome to the Quadratic Solver. This program will 
give your solutions as a complex number.
Quadratic equations take the following form:
		ax**2 + bx + c = 0
What are your choices for a, b and c?"""

# We define a function which prompts the user to enter the coefficients and proceeds to calculate and print
# 		the solutions in complex form.

a = float(raw_input("a: "))	# the float function converts the raw input into an integer
b = float(raw_input("b: "))	
c = float(raw_input("c: "))	

# To shorten the formula for the solution for x, we first calculate d as the discriminant.

d = b**2 - 4*a*c

# Now we complete the formula to obtain the two solutions

x1 = (-b - cmath.sqrt(d))/(2*a)
x2 = (-b + cmath.sqrt(d))/(2*a)

print "The solutions are %r and %r." % (x1, x2)
	


