v = ["A", "B", "A", "C", "C", "A", "C", "C", "A", "C", "C", "B", "A"]
r = [["A", 0], ["B", 0], ["C", 0]]

for i in range(len(v)): # I is true, len(v) is constant

    for j in range(len(r)): # II is true, len(r) is constant

        if v[i] == r[j][0]: # III is not really true, because it compares r[j][0] instead of r[j]

            r[j][1] += 1

print(r)
