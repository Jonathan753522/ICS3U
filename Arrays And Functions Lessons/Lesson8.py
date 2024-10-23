S = (input("input a string of DNA: "))
def validation(S):
  valid = True
  for D in range(len(S)):
    if not (S[D] == "A" or S[D] == "C" or S[D] == "G" or S[D] == "T"):
      print("Not valid: %s found in position %d." % (S[D], D + 1))
    return False
  return True

if validation("ATCAAGGCCTATTCCGGGAAAGG"):
  print("Valid")

if validation("TAGWGTGAAGTGCCATAGTT"):
  print("Valid")
  
if validation("CGCAGATGCCGCTGGTATGA"):
  print("Valid")
  
if validation("ATAGGTTAGCGGACCGAGAC"):
  print("Valid")
