import turtle
 
def main():
   
     turtle.hideturtle()
     square(85, 0, 200, "blue")

def square(x, y, width, color):
    turtle.penup()               # Raise the pen
    turtle.goto(x, y)            # Move to the specified location
    turtle.fillcolor(color)      # Set the fill color
    turtle.pendown()             # Lower the pen
    turtle.begin_fill()          # Start filling
    for count in range(4):       
          turtle.forward(width)
          turtle.left(90)
          turtle.end_fill()

if __name__ == '__main__':
    main()
            
