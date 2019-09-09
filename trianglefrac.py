import turtle
PROGNAME = 'Sierpinski triangle'

myPen = turtle.Turtle()
myPen.speed(8)
myPen.pencolor('blue')
# to define the three corners of the triangle
points = [[-175,-125],[0,175],[175,-125]] 

def Midpoint(p1,p2):
     return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) 
# recursively drawing smaller triangles
def Sierpinski(points,depth):

     myPen.up()
     myPen.goto(points[0][0],points[0][1])
     myPen.down()
     myPen.goto(points[1][0],points[1][1])
     myPen.goto(points[2][0],points[2][1])
     myPen.goto(points[0][0],points[0][1])
     # for the function to include itself until depth isn't there
     if depth>0:
          Sierpinski([points[0],
                        Midpoint(points[0], points[1]),
                        Midpoint(points[0], points[2])],
                   depth-1)
          Sierpinski([points[1],
                        Midpoint(points[0], points[1]),
                        Midpoint(points[1], points[2])],
                   depth-1)
          Sierpinski([points[2],
                         Midpoint(points[2], points[1]),
                         Midpoint(points[0], points[2])],
                   depth-1)
     else:
          pass
# to run the drawing
Sierpinski(points,6)