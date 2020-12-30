# Find the greatest common demoniator of two numbers

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

# try the function with a few examples
print(gcd(60, 96)) # should be 12
print(gcd(20, 8)) # should be 4