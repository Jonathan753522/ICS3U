"""
   Author : Jonathan Lee
   Revision date : 20 December 2024
   Program : Making A Word Finder
   Description : Finding words and dates using the date and word
   VARIABLE DICTIONARY :
    filename (str) = The file name/path for the xpm file
    month_to_number (List) list containing dates
    Dates (list) = Number of rows in the image
    Words (list) = Number of columns in the image
    ColorAmount (int) = Number of unique colors used in the image
    User_input (str) = User input in type string
    Userinp (bool) = Boolean value of if the userinp has entered valid input
    colorDefs (list) = List of colors and symbols used in the image
    imageData (list) = List of each line in the image with color information
"""
# Constants
filename = "wordle.dat"

# Month-to-number mapping
month_to_number = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

# Function to merge date components into a single integer
def merge(p, q, r):
    month = month_to_number[q.title()]  # Convert month to title case for consistency
    day = int(p)
    year = int(r)
    return year * 10000 + month * 100 + day

# Open the file
try:
    fh = open(filename, "r")
except:
    print("File not found.")
    exit()

# Arrays to store dates and words
Dates = []
Words = []

# Read data from file
for line in fh:
    parts = line.split()
    if len(parts) == 4:
        mon, day, year, word = parts
        date = merge(day, mon, year)
        Dates.append(date)
        Words.append(word)

# Function to sort the words and dates (synchronized)
def sort(words, dates):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i].upper() > words[j].upper():
                # Swap words
                words[i], words[j] = words[j], words[i]
                # Swap corresponding dates
                dates[i], dates[j] = dates[j], dates[i]

# Sort the words and dates alphabetically
sort(Words, Dates)

# Function to perform binary search by word
def isMatch(word, words, dates):
    low = 0
    high = len(words) - 1
    word = word.upper()

    while low <= high:
        mid = (low + high) // 2
        if words[mid].upper() == word:
            return dates[mid]
        elif words[mid].upper() < word:
            low = mid + 1
        else:
            high = mid - 1
    
    return 0

# Function to search by date
def search_by_date(year, month, day, dates, words):
    search_date = merge(str(day).zfill(2), month, str(year))
    # Check if date is too early or too late before continuing
    if search_date < 20210619:
        return ("%d is too early. Our records only go as late as 20240421. Please enter an earlier date." % search_date)
    elif search_date > 20240421:
        return ("%d is too late. Our records only go as late as 20240421. Please enter an earlier date." % search_date)
    
    # If valid date range, find the word
    if search_date in dates:
        index = dates.index(search_date)
        return words[index]
    else:
        return "Date %s not found in records." % search_date

# Main program loop
print("Welcome to the Wordle Database!")
valid = True
while (valid == True):
    action = input("Enter w if you are looking for a word, or d for a word on a certain date: ").strip().lower()

    if action == 'w':
        word = input("What word are you looking for? ").strip()
        date = isMatch(word, Words, Dates)
        word = word.upper()
        if date != 0:
            print("The word %s was the solution to the puzzle on %d" % (word, date))
            break
        else:
            print("%s was not found in the database." % (word))

    elif action == 'd':
        year = int(input("Enter the year: "))
        month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ").strip()
        day = int(input("Enter the day: "))

        result = search_by_date(year, month, day, Dates, Words)
        print(result)
        break
    else:
        print("Invalid option. Please enter 'w' or 'd'.")
