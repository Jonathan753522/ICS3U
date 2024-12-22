"""
   Author : Jonathan Lee
   Revision date : 20 December 2024
   Program : Making A Word Finder
   Description : Finding words and dates using the date and word
   VARIABLE DICTIONARY :
    filename (str) = The file name/path for the Wordle data file
    month_to_number (dict) = Dictionary mapping month abbreviations to corresponding month numbers
    word_list (list) = List containing words from the Wordle data file
    date_list (list) = List containing merged date integers from the Wordle data file
    Og_dates (list) = Copy of date_list, preserving the original order of dates
    Og_words (list) = Copy of word_list, preserving the original order of words
    start_date (int) = The earliest date (in integer form) from the data
    end_date (int) = The latest date (in integer form) from the data
    is_valid (bool) = Boolean flag indicating whether the user input is valid
    user_option (str) = Stores the user's choice ('w' for word search, 'd' for date search)
    user_word (str) = Stores the word input by the user for word search
    date_input (int) = Merged integer representing the date input by the user for date search
    year_input (str) = Year input by the user for date search
    month_input (str) = Month input by the user for date search (3-letter abbreviation)
    day_input (str) = Day input by the user for date search
    word_date (int) = Date corresponding to the searched word, if found
    word_for_date (str) = Word corresponding to the searched date, if found
    file_handle (file object) = Handle for reading the Wordle data file
    file_lines (list) = List of lines read from the Wordle data file
"""

# Constants
filename = "wordle.dat"

# Month-to-number mapping
month_to_number = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

# Function to merge date components into a single integer
def merge_date(year, month, day):
    try:
        month_num = month_to_number.get(month.title(), -1)
        if month_num == -1:
            return 0  # Return 0 to indicate invalid month
        return int(year) * 10000 + month_num * 100 + int(day)
    except:
        return 0

# Function to perform merge sort on two arrays
def merge_sort(list1, list2, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(list1, list2, left, mid)
        merge_sort(list1, list2, mid + 1, right)
        merge(list1, list2, left, mid, right)

# Function to merge two sorted arrays
def merge(list1, list2, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L1 = [0] * n1
    R1 = [0] * n2
    L2 = [0] * n1
    R2 = [0] * n2
    for i in range(n1):
        L1[i] = list1[left + i]
        L2[i] = list2[left + i]
    for j in range(n2):
        R1[j] = list1[mid + 1 + j]
        R2[j] = list2[mid + 1 + j]
    
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L1[i] <= R1[j]:
            list1[k] = L1[i]
            list2[k] = L2[i]
            i += 1
        else:
            list1[k] = R1[j]
            list2[k] = R2[j]
            j += 1
        k += 1
    while i < n1:
        list1[k] = L1[i]
        list2[k] = L2[i]
        i += 1
        k += 1
    while j < n2:
        list1[k] = R1[j]
        list2[k] = R2[j]
        j += 1
        k += 1

# Function to search for a word or date in a sorted array
def search_match(query, sorted_list, reference_list):
    index = binary_search(sorted_list, 0, len(reference_list) - 1, query)
    if index != -1:
        return reference_list[index]
    return 0

# Function to perform binary search on a sorted array
def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    return -1

# Open the file containing Wordle data
file_name = filename
file_handle = open(file_name, "r")

# Read all lines from the file
file_lines = file_handle.readlines()
for i in range(len(file_lines)):
    file_lines[i] = file_lines[i].strip()

# Initialize lists to store words and dates
word_list = []
date_list = []
for line in file_lines:
    month_str, day_str, year_str, word = line.split()
    merged_date = merge_date(year_str, month_str, day_str)
    date_list.append(merged_date)
    word_list.append(word)

# Close the file
file_handle.close()

# Get the start and end dates from the date_list
start_date = date_list[0]
end_date = date_list[-1]

# Create a copy of date_list and word_list to maintain the original order
Og_dates = date_list.copy()
Og_words = word_list.copy()

# Sort the word_list and date_list using merge_sort
merge_sort(word_list, date_list, 0, len(word_list) - 1)

print("Welcome to the Wordle Database!")
is_valid = False
user_option = ""

# Loop until valid input
while not is_valid:
    user_option = input("Enter 'w' to search for a word, or 'd' to search by date: ").lower()
    if user_option in ["w", "d"]:
        is_valid = True

if user_option == "w":
    is_valid = False
    # Loop until valid input
    while not is_valid:
        user_word = input("What word are you looking for? ").upper()
        if len(user_word) == 5:
            is_valid = True
    # Check if the word matches any in the database
    word_date = search_match(user_word, word_list, date_list)
    if word_date:
        print("The word %s was the solution to the puzzle on %d." % (user_word, word_date))
    else:
        print("%s was not found in the database." % (user_word))

elif user_option == "d":
    is_valid = False
    # Loop until valid input
    while not is_valid:
        year_input = input("Enter the year: ")
        month_input = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        day_input = input("Enter the day: ")
        date_input = merge_date(year_input, month_input, day_input)
        if date_input != 0:
            is_valid = True
    # Check if the date matches any in the database and get the corresponding word
    word_for_date = search_match(date_input, Og_dates, Og_words)
    if date_input < start_date:
        print("%s is too early. No Wordles occurred before %d. Enter a later date." % (date_input, start_date))
    elif date_input > end_date:
        print("%s is too late. No Wordles occurred before %s. Our records only go as late as %s. Please enter an earlier date." % (date_input ,end_date, date_input))
    elif word_for_date:
        print("The word entered on %s was %s." % (date_input, word_for_date))
