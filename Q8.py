def cont(n):

    a = 0

    while n >= a:

        print(str(a) + "\n")

        a = a + 1

    return

def contII(n):

    a = 0

    while n >= a:

        a = a + 1

        print(str(a) + "\n")

    return


def contIII(n):

    a = 0

    while n > a:

        print(str(a) + "\n")

        a = a + 1

    return print(str(a))

print("Answer without changes:")
cont(5)
print("Answer with changes proposed in II:")
contII(5)
print("Answer with changes proposed in III:")
contIII(5)

# If we assume that the absence of the last \n doesn't matter (which is the case in every sober online judge), then III is correct.
# I is not correct because it's >=, not >
