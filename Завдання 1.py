n = int(input("ввеідіть число n: "))
a = [int(input()) for i in range(n)]
f = 0
for element in a:
    if element >= 0:
        f = str(element)
print(min(f))
