import turtle

my_pen = turtle.Turtle()
my_pen.speed(8)
my_pen.pencolor('blue')
# corners [of the triangle] name shortened for cleanliness
corners = [[-175,-125] ,[0,175], [175,-125]] 

def midpoint_between(p1, p2):
     return ( (p1[0] + p2[0])/2, (p1[1] + p2[1])/2 ) 
     
# to recursively draw smaller triangles
def sierpinskize(corners, depth):
     my_pen.up()
     my_pen.goto(corners[0][0],corners[0][1])
     my_pen.down()
     my_pen.goto(corners[1][0],corners[1][1])
     my_pen.goto(corners[2][0],corners[2][1])
     my_pen.goto(corners[0][0],corners[0][1])
     # for the function to include itself until depth isn't there
     if depth>0:
          sierpinskize([corners[0],
                        midpoint_between(corners[0], corners[1]),
                        midpoint_between(corners[0], corners[2])],
                   depth-1)
          sierpinskize([corners[1],
                        midpoint_between(corners[0], corners[1]),
                        midpoint_between(corners[1], corners[2])],
                   depth-1)
          sierpinskize([corners[2],
                         midpoint_between(corners[2], corners[1]),
                         midpoint_between(corners[0], corners[2])],
                   depth-1)
     else:
          pass
def main():
    sierpinskize(corners, 6)

if __name__ == '__main__':
     main()
