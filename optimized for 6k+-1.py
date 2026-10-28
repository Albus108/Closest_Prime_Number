def P(n):
    if n<2:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i*i<=n:
        if n%i==0 or n%(i + 2)==0:
            return False
        i += 6
    return True

def closest_primes(x):
    if P(x):
        return x, None
    distance=1
    while True:
        lower=x-distance
        upper=x+distance

        lower_is_prime=lower>=2 and P(lower)
        upper_is_prime=P(upper)

        if lower_is_prime and upper_is_prime:
            return lower, upper

        if lower_is_prime:
            return lower, None

        if upper_is_prime:
            return upper, None

        distance=distance+1

def main():
    try:
        x = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if P(x):
        print(f"{x} is prime.")
        return

    first, second = closest_primes(x)

    if second is not None:
        print(f"Closest prime numbers to {x} are {first} and {second}.")
    else:
        print(f"Closest prime number to {x} is {first}.")

if __name__ == "__main__":
    main()