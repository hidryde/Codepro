A = int(input())
B = int(input())
# we took the inputs
for A in range(A,B+1):   # A in range (A,B)
    if A == 1:
        B = "one"
    if A == 2:
        B = "two"
    if A == 3:
        B = "three"
    if A == 4:
        B = "four"
    if A == 5:
        B = "five"
    if A == 6:
        B = "six"
    if A == 7:
        B = "seven"
    if A == 8:
        B = "eight"
    if A == 9:
        B = "nine"
    if int(A)>9 and int(A)%2==0:
        B = "even"
    if int(A)>9 and int(A)%2!=0:
        B = "odd"
    print(B)
