'''for problem e - recursive dijkstra's algorithm'''
'''first try weeee'''
from re import X


inputLine = "84 268"

'''inputLine = inputLine.split()
inputLine = [int(i) for i in inputLine]
a = inputLine[0]
b = inputLine[1]

def gcd(a,b):
    if a==b:
        print(a)
    elif a > b:
        a = a - b
        gcd(a,b)
    elif a < b:
        b = b - a
        gcd(a,b)

gcd(a,b)'''

'''for problem f'''
hailstoneInput = "7"
hailstoneInput = int(hailstoneInput)

def hailstone(n):
    sequence = []
    looping = True
    while looping == True:
        if n == 1:
            sequence.append(1)
            looping = False
        elif (n % 2 ) == 0:
            sequence.append(n)
            n = n/2
            hailstone(n)
        elif (n % 2) == 1:
            sequence.append(n)
            n = (3*n + 1)
            hailstone(n)
    return(sum(sequence))
'''print(hailstone(hailstoneInput))'''

'''for problem g'''
inputLine1 = "10 1 0"
inputLine1 = inputLine1.split()
inputLine1 = [int(i) for i in inputLine1]
n = inputLine1[0]
i = inputLine1[1]
x = inputLine1[2]

inputLine2 = "7 2 2 1 1 1 1 2 3 5"
a = inputLine2.split()
a = [int(i) for i in a]
v = a[i]

def fill(a, n, i, v, x):
    looping = True
    while looping == True:
        if i < 0 or i >= n:
            looping = False
        elif a[i] != v:
            looping = False
        elif a[i] == x:
            looping = False
        else:
            a[i] = x
            fill(a, n, i-1, v, x)
            fill(a, n, i+1, v, x)
    looping = False
    a = [str(k) for k in a]
    new = ' '.join(a)
    return(new)

print(fill(a, n, i, v, x))

'''for problem h'''




