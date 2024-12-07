"""
   Author : Jonathan Lee
   Revision date : 6 December 2024
   Program : Making A Graphics Plotter using Turtle
   Description : Choose an image to draw using the code
   VARIABLE DICTIONARY :
    filename (str) = The file name/path for the xpm file
    rotate (bool) = Boolean value of if the image will be rotated
    rows (int) = Number of rows in the image
    cols (int) = Number of columns in the image
    ColorAmount (int) = Number of unique colors used in the image
    User_input (str) = User input in type string
    Userinp (bool) = Boolean value of if the userinp has entered valid input
    colorDefs (list) = List of colors and symbols used in the image
    imageData (list) = List of each line in the image with color information
"""

import turtle            # Import the turtle graphics library for drawing
turtle.bgcolor("gray20") # Set the background color of the screen to a dark gray
turtle.tracer(0,0)       # Turn off screen updates to speed up the plotting process
t = turtle.Turtle()      # Create a turtle object for plotting the image
t.hideturtle()           # Hide the turtle icon, so it's not visible during the drawing

# Functions
def modify(ln):
    #Removes unwanted characters (quotes and commas) from a line of text.
    modifyStr = ""
    badChars = ['"', ',']  # List of unwanted characters
    ln = ln.strip()        # Remove leading/trailing spaces
    for c in ln:           # Iterate through each character in the line
        if c not in badChars:   # If the character is not unwanted, add it to the modified string
            modifyStr = modifyStr + c
    return modifyStr

def plotIt(T, x, y, d, color):
   #Draws a dot of size `d` and color `color` at the position (x, y).
    T.penup()              # Lift the pen to move to the desired position
    T.goto(x, y)           # Move the turtle to the specified (x, y) coordinates
    T.pendown()            # Lower the pen to start drawing
    T.dot(d, color)        # Draw a dot with the specified size and color
    T.penup()              # Lift the pen after drawing the dot

def drawImage(img, PixelSize, rows, cols, Xflip, Yflip):
    #Draws the image by iterating over each pixel, flipping it as necessary, and plotting each pixel with the correct color.
    Xdivide = int(-cols / 2)  # Set initial X position based on number of columns
    Ydivide = int(-rows / 2)  # Set initial Y position based on number of rows
    for x in range(len(img)):  # repeat through each row of the image
        Ydivide += 1
        for y in range(len(img[x])):  # repeat through each column in the row
            plotIt(t, Xdivide * PixelSize * Xflip, -Ydivide * PixelSize * Yflip, PixelSize, img[x][y])
            Xdivide += 1
        Xdivide = int(cols / 2) * -1  # Reset X position for the next row

def getImageAndColorData(fh, rows, cols):
    #Reads the image data and color definitions from the file. Returns imageData and colorDefs for use in drawing the image.
    imageData = []   # List to store the pixel colors of the image
    colorDefs = []   # List to store color mappings
    
    # Process the color definitions from the file
    for i in range(ColorAmount):
        colorLine = fh.readline()  # Read a line for color definition
        colorLine = modify(colorLine)  # Remove unwanted characters
        sym, c, color = colorLine.split()  # Split the line into symbol, count, and color
        if sym == '~':  # Replace '~' symbol with a space
            sym = ' '
        colorDefs.append([sym, color])  # Store the symbol and color pair
    
    # Process the image data
    for i in range(rows):
        row = fh.readline()  # Read a line representing a row of the image
        row = modify(row)  # Clean the line by removing unwanted characters
        rowArr = []  # List to store the colors for this row
        for j in range(len(row)):
            color = row[j]  # Get the symbol for the pixel
            for k in range(ColorAmount):
                if color == colorDefs[k][0]:  # Match the symbol to its color
                    color = colorDefs[k][1]
            rowArr.append(color)  # Add the color to the row
        imageData.append(rowArr)  # Add the row to the image data list
    
    return imageData, colorDefs  # Return the image data and color definitions

filename = ""  # Variable to hold the file name
rotate = False  # Boolean flag to check if the image should be rotated

# User input loop for selecting an image file
Userinp = False
while Userinp == False:
    User_input = input("Choose an option: A: rocky_bullwinkle_mod.xpm B: smiley_emoji_mod.xpm C: Enter a file name \n")
    if User_input.lower() == 'a':
        filename = "rocky_bullwinkle_mod.xpm"  # Default to rocky_bullwinkle_mod.xpm
        Userinp = True
    elif User_input.lower() == 'b':
        filename = "smiley_emoji_mod.xpm"  # Default to smiley_emoji_mod.xpm
        Userinp = True
    elif User_input.lower() == 'c':
        filename = input("Enter the file name: ")  # Prompt user to enter a custom file name
        Userinp = True

# User input loop for selecting whether to rotate the image
Userinp = False
while Userinp == False:
    User_input = input("Would You Like The Image Rotated (Y/N): ")
    if User_input.lower() == 'y':
        rotate = True  # Set rotate flag to True if user wants to rotate
        Userinp = True
    elif User_input.lower() == 'n':
        Userinp = True  # Set rotate flag to False if user does not want to rotate

fh = None
try:
    # Attempt to open the file for reading
    fh = open(filename, "r")
except:
    # If the file cannot be found or opened, print an error and exit
    print("File not found.")
    exit()

colorData = fh.readline()  # Read the first line for image metadata (dimensions and color count)
colorData = modify(colorData)  # Clean the metadata line
rows, cols, ColorAmount = (0,0,0)  # Initialize variables for rows, cols, and color count
try:
    # Try splitting the colorData into rows, cols, and ColorAmount
    cols, rows, ColorAmount = colorData.split()
except:
    # Handle case where there is extra data in the colorData line
    cols, rows, ColorAmount, temp = colorData.split()

rows = int(rows)  # Convert the number of rows to an integer
cols = int(cols)  # Convert the number of columns to an integer
ColorAmount = int(ColorAmount)  # Convert the number of colors to an integer

# Get the image data and color definitions by reading the file
imageData, colorDefs = getImageAndColorData(fh, rows, cols)

fh.close()  # Close the file after reading

# Print the image's dimensions and color information
print("Dimensions: %d x %d" % (rows, cols))
print("Number of colors:", ColorAmount)
print("Colors:", colorDefs)

# Draw the image, rotating if necessary
if rotate:
    drawImage(imageData, 3, rows, cols, -1, -1)  # Draw rotated image
else:
    drawImage(imageData, 3, rows, cols, 1, 1)  # Draw non-rotated image

turtle.update()  # Update the screen with the drawn image
