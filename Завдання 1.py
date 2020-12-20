n = int(input("ввеідіть число n: "))
a = [int(input()) for i in range(n)]
b = []
for i in range(len(a)):
    if a[i] > 0:
        b.append(a[i])
f = min(b)
print(f)