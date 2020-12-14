import math

n = int(input("введіть число n: "))
b = int(input("введіть число b: "))
a = []
h = []
z=0
i=0
while n>i:
    a.append(math.factorial(i)*math.sin(i*b))
    i+=1
print(a)
while n>i:
   h.append(a[n-1]*a[n])
   i+=1
print(h)
z=min(h)