from math import sqrt

#Prime Numbers
x = int(input("Enter a number: "))

if x>1:
    for n in range(2, int(sqrt(x))+1):
        if (x%n) == 0:
            print(f"{x} is not a prime number")
            break
    else:
        print(f"{x} is a prime number")
else:
    print(f"Please enter an eligable value")

#Sieve of Erastosthenes
def soe(y):
    prime = [True for i in range(y+1)]
    z = 2
    while (z*z <= y):
        if (prime[z] == True):
            for i in range(z*z, y+1, z):
                prime[i] = False
        z+=1
    for z in range(2, y+1):
        if prime[z]:
            print(z)

y = int(input("Enter another number: "))
print(f"These are the prime numbers that are under {y}")
soe(y)

#LoveYou3000
a = 3000
for num in range(1, a+1):
    c = 0
    rev = 0
    temp = num
    for i in range(1, temp+1):
        if temp%i == 0:
            c += 1
    if c==2:
        while temp>0:
            rev = rev*10+(temp%10)
            temp //=10
        if rev == num:
            print(num)

#2 Digit Primes
primes = []

for num in range(2, 101):
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            prime = False
            break
    if prime:
        primes.append(num)

print(primes)