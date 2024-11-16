n = int(input("Enter the value of n : "))
i = 1
n1 = 2 ** i
n2 = 2 * n1
print(n1, n2)
j = 3
for j in range(n + 1):
    n3 = n1 * n2
    print(n3)
    n1 = n2
    n2 = n3