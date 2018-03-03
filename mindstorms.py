import turtle

def drawsquare():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2000)

    i=0
    for i in range (1,36):
    #while i < 100:
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(105)
        i=i+1
   
      
    

    
    window.exitonclick()


drawsquare()
