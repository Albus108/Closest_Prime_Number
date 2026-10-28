def P(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0: #checks whether the no. is even or not
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a factor, so it's not prime
    return True  # No factors found, it's prime

x=int(input("x: "))

if P(x):
    print(x,"is Prime")

else:
    y=x+1
    z=x-1
    while not P(y):
        y=y+1
    a=abs(x-y)

    while z>=2 and not P(z):
        z=z-1
    if z<2:
        b=float("inf")
    else:
        b=abs(x-z)

    if a<b:
        print("Closest prime number to ",x,"is",y)
    elif a==b:
        print("Closest prime numbers to ",x,"are",y,"and",z)
    else:
        print("Closest prime number to ",x,"is",z)