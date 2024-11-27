import turtle
turtle.bgcolor("gray40")
T = turtle.Turtle()


#Functions
def modify(ln):
    mod_string = ""
    badChars = ['"', ',']
    ln = ln.strip()
    for c in ln:
        if c not in badChars:
            mod_string = mod_string + c
    return mod_string

def PlotIt(T, x, y, d, color):
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(d, color)
    T.penup()

filename = "rocky_bullwinkle_mod.xpm"
fh = open(filename, "r")

colorData = fh.readline()
colorData = modify(colorData)
rows, cols, numColors = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)

Userinp = input("Press R if you want your image rotated")
if (userinp.lower() == "R"):
    colorDefs = []
    for i in range(numColors):
        colorLine = fh.readline() 
        colorLine = modify(colorLine)
        sym, c, color = colorLine.split()
        if sym == '~':
            sym = " "
        colorDefs.append([sym, color])

    imageData = []
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

    print("Dimensions: %d x %d" % (rows, cols))
    print("Number of colors:", numColors)
    print("Colors:", colorDefs)
    for i in imageData:
        print(i)

    fh.close()
