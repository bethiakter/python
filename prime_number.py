def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True



n = int(input('Enter a number:'))

l = []
i = 2

while len(l) < n:
    if isPrime(i) == True:
        l.append(i)
        i = i + 1
    else:
        i = i + 1

print(l)