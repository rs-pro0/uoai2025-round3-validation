def Fib(n):
    F0 = [1, 1]

    for i in range(2, n):

        F0.append(F0[i-2] + F0[i-1])

    return print(F0)

assert(Fib(6)==None)
