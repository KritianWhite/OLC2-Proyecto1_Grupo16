def factorial(n):
    if n==0 or n==1:
        return 1
    elif n > 1: 
        return n*factorial(n-1)


def ackerman(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackerman( m - 1, 1)
    else:
        return ackerman( m - 1, ackerman(m, n - 1 ))

print(factorial(4))
print(ackerman(3, 5))

