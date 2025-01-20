"""
   Author : Jonathan Lee
   Revision date : 20 December 2024
   Program : Credit Card Revisor
   Description : Checks to see if you need to renew your card or if its expired
   VARIABLE DICTIONARY :
    filename: str - Name of the file
    fh: file object - File handle
    Names: list - List of Names (first and last)
    CCnums: list - List of credit card numbers
    CCtypes: list - List of credit card types
    ExpiryDates: list - List of expiry dates
    lines: list - List of all the lines in file
    FirstLine: str - First line of the file (to be removed from lines)
    OutputFile: file object - File handle for the output file
    ExpiredText: str - Text to display when expired
"""

# Define the input filename
filename = "data.dat"


def merge_sort(list1, list2, list3, list4, left, right):
    
    #Recursive function to implement merge sort for four lists.
    #This will sort all the lists based on ExpiryDates.
    
    if left < right:
        mid = left + (right - left) // 2  # Find the middle index
        # Recursively split the lists into two halves
        merge_sort(list1, list2, list3, list4, left, mid)
        merge_sort(list1, list2, list3, list4, mid + 1, right)
        # Merge the sorted halves
        merge(list1, list2, list3, list4, left, mid, right)

# Function to merge two sorted halves into one sorted list
def merge(list1, list2, list3, list4, left, mid, right):

    #Merge function to combine two sorted sub-arrays into one sorted array.
    #This function merges four lists (ExpiryDates, Names, CCnums, CCtypes) based on ExpiryDates.
    
    n1 = mid - left + 1  # Size of left sub-array
    n2 = right - mid  # Size of right sub-array
    
    # Temporary arrays to hold values from the two halves
    L1 = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R1 = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2

    # Copy data into temporary arrays
    for i in range(0, n1):
        L1[i] = list1[left + i]
        L2[i] = list2[left + i]
        L3[i] = list3[left + i]
        L4[i] = list4[left + i]
    
    for j in range(0, n2):
        R1[j] = list1[mid + 1 + j]
        R2[j] = list2[mid + 1 + j]
        R3[j] = list3[mid + 1 + j]
        R4[j] = list4[mid + 1 + j]
        
    # Merging the arrays back into the original lists
    i = 0  # Initial index of left sub-array
    j = 0  # Initial index of right sub-array
    k = left  # Initial index of the merged array
    while i < n1 and j < n2:
        if L1[i] <= R1[j]:
            list1[k] = L1[i]
            list2[k] = L2[i]
            list3[k] = L3[i]
            list4[k] = L4[i]
            i += 1
        else:
            list1[k] = R1[j]
            list2[k] = R2[j]
            list3[k] = R3[j]
            list4[k] = R4[j]
            j += 1
        k += 1
    
    # Copy remaining elements from left sub-array, if any
    while i < n1:
        list1[k] = L1[i]
        list2[k] = L2[i]
        list3[k] = L3[i]
        list4[k] = L4[i]
        i += 1
        k += 1
    
    # Copy remaining elements from right sub-array, if any
    while j < n2:
        list1[k] = R1[j]
        list2[k] = R2[j]
        list3[k] = R3[j]
        list4[k] = R4[j]
        j += 1
        k += 1


# Open the data file for reading
fh = open(filename, 'r')

# Initialize lists to hold names, credit card numbers, types, and expiry dates
Names = []
CCnums = []
CCtypes = []
ExpiryDates = []

# Read all lines from the file
lines = fh.readlines()

# Remove the first line (header) of the file
FirstLine = lines.pop(0)

# Process each line in the file
for line in lines:
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    # Combine first and last name
    name = given_name + ' ' + surname
    Names.append(name)
    CCtypes.append(cc_type)
    CCnums.append(cc_number)
    
    # Format expiry month to ensure it's two digits
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    
    # Create expiry date in the format YYYYMM (e.g., 202512 for December 2025)
    expiry_date = exp_yr + exp_mo
    ExpiryDates.append(int(expiry_date))

# Close the input file
fh.close()

# Sort the data based on expiry dates using merge sort
merge_sort(ExpiryDates, Names, CCnums, CCtypes, 0, len(ExpiryDates) - 1)

# Open an output file to write the results
OutputFile = open("JonathanCodeOutput.txt", "w")

# Check each credit card's expiry date and write the result to the output file
for i in range(len(ExpiryDates)):
    # If the expiry date is greater than January 2025 (i.e., not expired)
    if ExpiryDates[i] > 202501:
        break
    
    # Set the expired text based on the expiry date
    ExpiredText = "RENEW IMMEDIATELY" if ExpiryDates[i] < 202501 else "EXPIRED"
    
    # Print the credit card information to the console
    print("%-35s %-15s %-20s %-8s %-15s" % (Names[i], CCtypes[i], CCnums[i], ExpiryDates[i], ExpiredText))
    
    # Write the credit card information to the output file
    OutputFile.write("%-35s %-15s %-20s %-8s %-15s\n" % (Names[i], CCtypes[i], CCnums[i], ExpiryDates[i], ExpiredText))

# Close the output file
OutputFile.close()

