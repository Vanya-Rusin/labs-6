import math

n = int(input("введіть число n: "))
b = int(input("введіть число b: "))
a = []
h = []
z=0
i=1
while n >= i:
    a.append( math.factorial(i)*math.sin(i*b))
    i+=1
i = 1
while n > i:
    h.append (a[i-1] * a[i])
    i += 1
print(min(h))