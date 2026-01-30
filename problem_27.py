def gcd(a, b):
    while b!= 0:
        temp= b
        b = a % b
        a = temp
    return a

print(f"GCD of 48 and 18: {gcd(48, 18)}")
