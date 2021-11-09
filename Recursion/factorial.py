import sys
def factorial(n):
    assert n>=0 and int(n)==n,'the number must be positive.' #assert true statement, (if not true ~ the number must..)(otherwise case)
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(10))