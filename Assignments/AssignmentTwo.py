import turtle  # should be at the top of your code

# Constants and Initialization
turtle.bgcolor("gray40")  # dark gray
turtle.tracer(0, 0)  # turns off updates to speed up plotting
t = turtle.Turtle()  # makes it easier to call the plotting functions
t.hideturtle()  # prevents the plotter sprite from appearing in your image


def Modify(ln):
    # Remove unwanted characters (e.g., quotation marks and commas) from a string.
    return ''.join([c for c in ln.strip() if c not in ['"', ',']])


def plotIt(T, x, y, size, color):
    # Plot a single pixel at position (x, y) with a given size and color.
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(size, color)
    T.penup()


def LoadandDrawimage(filename, rotate=False):
    # Load image data from a file and draw it on the screen with optional rotation.
    file_handler = open(filename, "r")
    try:
        # Read the first line with the dimensions and number of colors
        color_data = Modify(file_handler.readline())
        
        # Split the color data line, handle possible extra values
        color_data_parts = color_data.split()
        if len(color_data_parts) < 3:
            ValueError("Invalid color data format: {}".format(color_data))
        
        rows, cols, numColors = map(int, color_data_parts[:3])  # Use only the first three values

        # Read color definitions
        colorDefs = []
        for _ in range(numColors):
            line = Modify(file_handler.readline())
            sym, c, color = line.split()
            colorDefs.append([sym if sym != '~' else ' ', color])

        # Read image data and map color symbols to actual colors
        image_data = []
        for _ in range(rows):
            row = Modify(file_handler.readline())
            row_data = []
            for color in row:
                # Check if color exists in colorDefs, otherwise use a default color
                matched_color = None
                for color_def in colorDefs:
                    if color_def[0] == color:
                        matched_color = color_def[1]
                        break
                if matched_color:
                    row_data.append(matched_color)
                else:
                    row_data.append("black")  # Default color for unmatched symbols
            image_data.append(row_data)
        file_handler.close()

    print("\nDimensions: %d x %d" % (rows, cols))
    print("Number of colors:", numColors)
    print("Colors:", colorDefs)

    # Draw the image with or without rotation
    x_offset = -cols // 2
    y_offset = -rows // 2
    x_rot = -1 if rotate else 1
    y_rot = -1 if rotate else 1

    for x in range(len(image_data)):
        y_offset += 1
        for y in range(len(image_data[x])):
            plotIt(t, x_offset * 3.5 * x_rot, -y_offset * 3.5 * y_rot, 3.5, image_data[x][y])
            x_offset += 1
        x_offset = -cols // 2


def getuserinput():
    """Get user input for the file and rotation choice."""
    filename = ""
    rotate = False
    Userinp = True
    # Get file choice
    while Userinp == True:
        user_input = input("Choose an option:\n A: rocky_bullwinkle_mod.xpm \n B: smiley_emoji_mod.xpm \n C: Enter a file name\n")
        if user_input.lower() == 'a':
            filename = "rocky_bullwinkle_mod.xpm"
            Userinp = False
            break
        elif user_input.lower() == 'b':
            filename = "smiley_emoji_mod.xpm"
            Userinp = False
            break
        elif user_input.lower() == 'c':
            filename = input("Enter the file name: ")
            Userinp = False
            break
        else:
            print("Invalid choice. Please try again.")

    # Get rotation choice
    while Userinp == False:
        user_input = input("Would you like to rotate the image (Y/N): ")
        if user_input.lower() == 'y':
            rotate = True
            Userinp = True
            break
        elif user_input.lower() == 'n':
            rotate = False
            Userinp = True
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    return filename, rotate


# Main Program Execution
filename, rotate = getuserinput()
LoadandDrawimage(filename, rotate)

