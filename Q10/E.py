A = [99, 45, 39, 36, 28, 21]

x = [72]

for i in range(len(x)):

    x = x + [(A[i] - x[i])]

print(A)
