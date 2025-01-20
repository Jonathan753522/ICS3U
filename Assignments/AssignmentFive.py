"""
   Author : Jonathan Lee
   Revision date : 20 December 2024
   Program : Credit Card Revisor
   Description : Checks to see if you need to renew your card or if its expired
   VARIABLE DICTIONARY :
    
"""

filename = "data.dat"


def merge_sort(list1, list2, list3, list4, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(list1, list2, list3, list4, left, mid)
        merge_sort(list1, list2, list3, list4, mid + 1, right)
        merge(list1, list2, list3, list4, left, mid, right)

# Function to merge two sorted arrays
def merge(list1, list2, list3, list4, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L1 = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R1 = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2
    for i in range(0, n1):
        L1[i] = list1[left + i]
        L2[i] = list2[left + i]
        L3[i] = list3[left + i]
        L4 [i] = list4[left + i]
    for j in range(0, n2):
        R1[j] = list1[mid + 1 + j]
        R2[j] = list2[mid + 1 + j]
        R3[j] = list3[mid + 1 + j]
        R4[j] = list4[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  
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
    while i < n1:
        list1[k] = L1[i]
        list2[k] = L2[i]
        list3[k] = L3[i]
        list4[k] = L4[i]
        i += 1
        k += 1
    while j < n2:
        list1[k] = R1[j]
        list2[k] = R2[j]
        list3[k] = R3[j]
        list4[k] = R4[j]
        j += 1
        k += 1



fh = open(filename, 'r')

names = []
CCnums = []
CCtypes = []
ExpiryDates = []

lines = fh.readlines()
first_line = lines.pop(0)
for line in lines:
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    name = given_name + ' ' + surname
    names.append(name)
    CCtypes.append(cc_type)
    CCnums.append(cc_number)
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    expiry_date = exp_yr + exp_mo
    ExpiryDates.append(int(expiry_date))

fh.close()

merge_sort(ExpiryDates, names, CCnums, CCtypes, 0, len(ExpiryDates) - 1)
output_file = open("output.txt","w")
for i in range(len(ExpiryDates)):
    if ExpiryDates[i] > 202501:
        break
    expired_text = "RENEW IMMEDIATELY"
    if ExpiryDates[i] < 202501:
        expired_text = "EXPIRED"
    print("%-35s %-15s %-20s %-8s %-15s" % (names[i], CCtypes[i], CCnums[i], ExpiryDates[i], expired_text))
    output_file.write("%-35s %-15s %-20s %-8s %-15s\n" % (names[i], CCtypes[i], CCnums[i], ExpiryDates[i], expired_text))
output_file.close()

