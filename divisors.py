
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

def divisors(a,b):
    if (b==0):
        return a
    else:
        return divisors(b,a%b)

print(divisors(a,b))