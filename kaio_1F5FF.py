#Pixel Art - http://www.101computing.net/pixel-art-in-python/

import turtle

myPen = turtle.Turtle()
myPen._tracer(0)
myPen.speed(0)
myPen.color("#000000")


# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)
	
boxSize = 10	
#Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)

##Here is an example of how to draw a box	
#box(boxSize)

##Here are some instructions on how to move "myPen" around before drawing a box.
#myPen.setheading(0) #point to the right, 90 to go up, 180 to go to the left 270 to go down
#myPen.penup()
#myPen.forward(boxSize)
#myPen.pendown()

#Here is how your PixelArt is stored (using a "list of lists")

pixels = []
zero_sixteen = ["" for i in range(32)]

for i in range(16):
    pixels.append(zero_sixteen.copy())

def drawLine(c1,r1,c2,r2,color):
    if r1 == r2:
        for i in range(c1,c2):
            drawPixel(i,r1,color)
            print(1)
    elif c1 == c2:
        for i in range(r1,r2):
            drawPixel(c1,i,color)
            print(2)
    elif c1 != c2 and r1!=r2:
        
        if (abs(c1-c2) - abs(r1 - r2)) == 0:
            upright = (c2>c1 and r1>r2)
            downright = (c2>c1 and r2>r1)
            upleft = (c1>c2 and r1>r2)
            downleft = (c1>c2 and r2>r1)
            if upright:
                cm = 1
                rm = -1
            if downright:
                cm = 1
                rm = 1
            if upleft:
                cm = -1
                rm = -1
            if downleft:
                cm = -1
                rm = 1
            for i in range(0,abs(r1-r2)):
                drawPixel(c1+cm*i,r1+rm*i,color)
    
            
def drawPixel(column,row,color):
    if (column > 31 or row > 31 or column < 0 or row < 0):
        raise IndexError("Out of Bounds")

    else:
        pixels[row][column] = color
def showdrawing():
    for i in range (0,len(pixels)):
        for j in range (0,len(pixels[i])):
            if pixels[i][j]:
                myPen.fillcolor(pixels[i][j])
                myPen.pencolor(pixels[i][j])
                box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.setheading(270) 
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180) 
        myPen.forward(boxSize*len(pixels[i]))
        myPen.setheading(0)
        myPen.pendown()
    myPen.getscreen().update()

#drawLine(15,0,25,10,"red")
#drawLine(0,0,10,10,"blue")
#drawPixel(31,31,"red")
#drawLine(10,10,20,10,"red")
'''drawLine(10,12,20,12,"red") #boca
drawLine(11,13,19,13,"red")
drawLine(12,14,18,14,"red")
drawLine(10,7,10,9,"red")	#olho esquerdo
drawLine(19,7,19,9,"red")	#olho direito
drawLine(9,4,11,6,"red") #sobrancelha esquerda
drawLine(19,5,21,3,"red")#sobrancelha direita'''

'''drawLine(0,0,5,0,"red")
drawLine(0,1,5,1,"orange")   # arco-íris
drawLine(0,2,5,2,"yellow")
drawLine(0,3,5,3,"green")
drawLine(0,4,5,4,"blue")
drawLine(0,5,5,5,"purple")'''

'''drawLine(0,0,5,5,"red")
drawLine(5,5,0,10,"red")
drawLine(6,2,8,2,"red")
drawLine(6,8,8,8,"red")		# >:D
drawLine(10,0,10,10,"red")
drawLine(10,0,15,5,"red")
drawLine(10,10,15,5,"red")
drawPixel(15,5,"red")'''

'''drawLine(0,0,0,10,"red")
drawLine(0,5,5,0,"red")
drawLine(0,5,5,10,"red")
drawLine(7,0,7,10,"red")
drawLine(11,0,11,10,"red")
drawLine(7,0,11,0,"red")
drawLine(7,4,11,4,"red")	# KAIO
drawPixel(14,0,"red")
drawLine(14,2,14,10,"red")
drawLine(17,0,17,10,"red")
drawLine(23,0,23,10,"red")
drawLine(17,0,23,0,"red")
drawLine(17,9,23,9,"red")'''







showdrawing()