"""
   Author : Jonathan Lee
   Revison date : 6 December 2024
   Program : Making A Graphics Plotter using Turtle
   Description : choose an image to draw using the code
   VARIABLE DICTIONARY :
    filename (str) = The file name/path for the xpm file
    rotate (bool) = Boolean value of if the image will be rotated
    rows (int) = Number of rows
    cols (int) = Number of cols
    ColorAmount (int) = Number of colors
    User_input (str) = User input in type string
    Userinp (bool) = Boolean value of if the userinp has entered valid input
    colorDefs (list) = Array of the colors and symbols
    imageData (list) = Array of each line in the image with colors
"""

import turtle            # should be at the top of your code
turtle.bgcolor("gray40") # dark gray - try gray40 for a lighter gray
turtle.tracer(0,0)       # turns off updates to speed up plotting
t = turtle.Turtle()      # makes it easier to call the plotting functions
t.hideturtle()           # prevents the plotter sprite from appearing in your image

#Functions
def modify(ln):
    modifyStr = ""
    badChars = ['"', ',']
    ln = ln.strip()
    for c in ln:
        if c not in badChars:
            modifyStr = modifyStr + c
    return modifyStr

def plotIt(T, x, y, d, color):
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(d, color)
    T.penup()

def drawImage(img, PixelSize, rows, cols, Xflip, Yflip):
    Xdivide = int(-cols / 2)
    Ydivide = int(-rows / 2)
    for x in range(len(img)):
        Ydivide += 1
        for y in range(len(img[x])):
            plotIt(t, Xdivide * PixelSize * Xflip, -Ydivide * PixelSize * Yflip, PixelSize, img[x][y])
            Xdivide += 1
        Xdivide = int(cols / 2) * -1

def getImageAndColorData(fh, rows, cols):
    imageData = []
    colorDefs = []
    
    # Process the color definitions first
    for i in range(ColorAmount):
        colorLine = fh.readline() 
        colorLine = modify(colorLine)
        sym, c, color = colorLine.split()
        if sym == '~':
            sym = ' '
        colorDefs.append([sym, color])

    # Process the image data
    for i in range(rows):
        row = fh.readline()
        row = modify(row)
        rowArr = []
        for j in range(len(row)):
            color = row[j]
            for k in range(ColorAmount):
                if color == colorDefs[k][0]:
                    color = colorDefs[k][1]
            rowArr.append(color)
        imageData.append(rowArr)
    
    return imageData, colorDefs


filename = ""
rotate = False

Userinp = False
while Userinp == False:
    User_input = input("Choose an option: A: rocky_bullwinkle_mod.xpm B: smiley_emoji_mod.xpm C: Enter a file name \n")
    if User_input.lower() == 'a':
        filename = "rocky_bullwinkle_mod.xpm"
        Userinp = True
    elif User_input.lower() == 'b':
        filename = "smiley_emoji_mod.xpm"
        Userinp = True
    elif User_input.lower() == 'c':
        filename = input("Enter the file name: ")
        Userinp = True

Userinp = False
while Userinp == False:
    User_input = input("Would You Like The Image Rotated (Y/N): ")
    if User_input.lower() == 'y':
        rotate = True
        Userinp = True
    elif User_input.lower() == 'n':
        Userinp = True
fh = None
try:
    # Open the chosen file for reading
    fh = open(filename, "r")
except:
    # File is not found and exit the program
    print("File not found.")
    exit()

colorData = fh.readline()
colorData = modify(colorData)
rows, cols, ColorAmount = (0,0,0)
try:
    cols, rows, ColorAmount = colorData.split()
except:
    cols, rows, ColorAmount, temp = colorData.split()

rows = int(rows)
cols = int(cols)
ColorAmount = int(ColorAmount)

imageData, colorDefs = getImageAndColorData(fh, rows, cols)

fh.close()

print("Dimensions: %d x %d" % (rows, cols))
print("Number of colors:", ColorAmount)
print("Colors:", colorDefs)

if rotate:
    drawImage(imageData, 3, rows, cols, -1, -1)
else:
    drawImage(imageData, 3, rows, cols, 1, 1)
turtle.update()
