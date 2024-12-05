import turtle            # should be at the top of your code
turtle.bgcolor("gray40") # dark gray - try gray70 for a lighter gray
turtle.tracer(0,0)       # turns off updates to speed up plotting
t = turtle.Turtle()      # makes it easier to call the plotting functions
t.hideturtle()           # prevents the plotter sprite from appearing in your image

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

def drawImage(img, pixel_size, rows, cols, x_rot, y_rot):
    x_half = int(-cols / 2)
    y_half = int(-rows / 2)
    for x in range(len(img)):
        y_half += 1
        for y in range(len(img[x])):
            plotIt(t, x_half * pixel_size * x_rot, -y_half * pixel_size * y_rot, pixel_size, img[x][y])
            x_half += 1
        x_half = int(cols / 2) * -1

def getImageAndColorData(fh, rows, cols):
    imageData = []
    colorDefs = []
    
    # Process the color definitions first
    for i in range(numColors):
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
            for k in range(numColors):
                if color == colorDefs[k][0]:
                    color = colorDefs[k][1]
            rowArr.append(color)
        imageData.append(rowArr)
    
    return imageData, colorDefs


filename = ""
rotate = False

Userinp = False
while Userinp == False:
    user_input = input("Choose an option: \n A: rocky_bullwinkle_mod.xpm \n B: smiley_emoji_mod.xpm \n C: Enter a file name \n")
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
    user_input = input("Would you like to rotate the image (Y/N): ")
    if user_input.lower() == 'y':
        rotate = True
        Userinp = True
    elif user_input.lower() == 'n':
        Userinp = True

fh = open(filename, "r")

colorData = fh.readline()
colorData = modify(colorData)
rows, cols, numColors = (0,0,0)
try:
    rows, cols, numColors = colorData.split()
except:
    rows, cols, numColors, temp = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)

# Using the merged function to get both image data and color definitions
imageData, colorDefs = getImageAndColorData(fh, rows, cols)

fh.close()

print("\nDimensions: %d x %d" % (rows, cols))
print("Number of colors:", numColors)
print("Colors:", colorDefs)

# Main logic moved here for execution after processing input
if rotate:
    drawImage(imageData, 3.5, rows, cols, -1, -1)
else:
    drawImage(imageData, 3.5, rows, cols, 1, 1)

