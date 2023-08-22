def palindrome(n):
    rev = 0
    j = n
    while j > 0:
        rev = rev * 10 + j % 10
        j //=10
    return (n==rev)

ls1 = []

for i in range(100000,1000000):

    if palindrome(i):
        ls1.append(i)
print(ls1)
