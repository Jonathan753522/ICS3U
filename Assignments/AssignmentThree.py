import turtle            # should be at the top of your code
turtle.bgcolor("gray40") # dark gray - try gray40 for a lighter gray
turtle.tracer(0,0)       # turns off updates to speed up plotting
t = turtle.Turtle()      # makes it easier to call the plotting functions
t.hideturtle()           # prevents the plotter sprite from appearing in your image

#Functions
def modify(ln):
    mod_string = ""
    badChars = ['"', ',']
    ln = ln.strip()
    for c in ln:
        if c not in badChars:
            mod_string = mod_string + c
    return mod_string

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
    user_input = input("Choose an option: A: rocky_bullwinkle_mod.xpm B: smiley_emoji_mod.xpm C: Enter a file name \n")
    if user_input.lower() == 'a':
        filename = "rocky_bullwinkle_mod.xpm"
        Userinp = True
    elif user_input.lower() == 'b':
        filename = "smiley_emoji_mod.xpm"
        Userinp = True
    elif user_input.lower() == 'c':
        filename = input("Enter the file name: ")
        Userinp = True

Userinp = False
while Userinp == False:
    user_input = input("Would You Like The Image Rotated (Y/N): ")
    if user_input.lower() == 'y':
        rotate = True
        Userinp = True
    elif user_input.lower() == 'n':
        Userinp = True

fh = open(filename, "r")

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
