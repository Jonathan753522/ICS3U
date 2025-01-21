"""
   Author : Jonathan Lee
   Revision date : 20 December 2024
   Program : Credit Card Revisor
   Description : Checks to see if you need to renew your card or if it's expired.
   VARIABLE DICTIONARY :
    filename: str - Name of the file containing credit card data.
    fh: file object - File handle for reading the input file.
    Names: list - List containing full names (first and last) of cardholders.
    CCnums: list - List containing credit card numbers.
    CCtypes: list - List containing credit card types.
    ExpiryDates: list - List containing credit card expiry dates in YYYYMM format.
    lines: list - List of all lines in the input file.
    FirstLine: str - The first line of the file (header) to be removed from the lines.
    OutputFile: file object - File handle for writing the output results.
    ExpiredText: str - Text to display when the card is expired or requires renewal.
"""

# Define the input filename for the credit card data
filename = "data.dat"

# Recursive function to perform merge sort on four lists based on expiry dates
def merge_sort(list1, list2, list3, list4, left, right):
    # Base case: if the left index is less than the right index
    if left < right:
        mid = left + (right - left) // 2  # Calculate the middle index
        # Recursively sort the two halves of the lists
        merge_sort(list1, list2, list3, list4, left, mid)
        merge_sort(list1, list2, list3, list4, mid + 1, right)
        # Merge the two sorted halves back together
        merge(list1, list2, list3, list4, left, mid, right)

# Function to merge two sorted sub-arrays into one sorted array
def merge(list1, list2, list3, list4, left, mid, right):
    # Calculate the size of the left and right sub-arrays
    n1 = mid - left + 1
    n2 = right - mid

    # Temporary arrays to hold values from the two halves
    L1 = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R1 = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2

    # Copy data from the original lists into temporary arrays
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
    
    # Merging the two sorted sub-arrays back into the original lists
    i = 0  # Index for the left sub-array
    j = 0  # Index for the right sub-array
    k = left  # Index for the merged list

    while i < n1 and j < n2:
        if L1[i] <= R1[j]:  # Compare expiry dates
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
    
    # Copy remaining elements from the left sub-array, if any
    while i < n1:
        list1[k] = L1[i]
        list2[k] = L2[i]
        list3[k] = L3[i]
        list4[k] = L4[i]
        i += 1
        k += 1
    
    # Copy remaining elements from the right sub-array, if any
    while j < n2:
        list1[k] = R1[j]
        list2[k] = R2[j]
        list3[k] = R3[j]
        list4[k] = R4[j]
        j += 1
        k += 1

# Open the input file in read mode to process the credit card data
fh = open(filename, 'r')

# Initialize lists to store names, credit card numbers, types, and expiry dates
Names = []
CCnums = []
CCtypes = []
ExpiryDates = []

# Read all lines from the file
lines = fh.readlines()

# Remove the first line (header) from the list of lines
FirstLine = lines.pop(0)

# Loop through each line to process the data
for line in lines:
    GivenName, surname, CCtype, CCnumber, ExpMo, ExpYear = line.strip().split(',')
    # Combine first and last names to create the full name
    name = GivenName + ' ' + surname
     # Add name to names list
    Names.append(name)
   # Add CCtypes to list
    CCtypes.append(CCtype)
   # Add cc_number to list
    CCnums.append(CCnumber)
    
    # Ensure the expiry month is two digits (e.g., '09' instead of '9')
    if len(ExpMo) == 1:
        ExpMo = '0' + ExpMo
    
    # Create expiry date in YYYYMM format (e.g., 202512 for December 2025)
    ExpiryDate = ExpYear + ExpMo
    ExpiryDates.append(int(ExpiryDate))

# Close the input file after processing all lines
fh.close()

# Sort the data by expiry dates using merge sort
merge_sort(ExpiryDates, Names, CCnums, CCtypes, 0, len(ExpiryDates) - 1)

# Open the output file in write mode to store the results
OutputFile = open("JonathanCodeOutput.txt", "w")

# Loop through the sorted lists to check each credit card's expiry date
for i in range(len(ExpiryDates)):
    # If the expiry date is greater than January 2025, stop checking further
    if ExpiryDates[i] > 202501:
        break
    
    # Set the expired text based on the expiry date
    ExpiredText = "RENEW IMMEDIATELY" if ExpiryDates[i] < 202501 else "EXPIRED"
    
    # Print the credit card details to the console
    print("%-35s %-15s %-20s %-8s %-15s" % (Names[i], CCtypes[i], CCnums[i], ExpiryDates[i], ExpiredText))
    
    # Write the credit card details to the output file
    OutputFile.write("%-35s %-15s %-20s %-8s %-15s\n" % (Names[i], CCtypes[i], CCnums[i], ExpiryDates[i], ExpiredText))

# Close the output file after writing the results
OutputFile.close()

