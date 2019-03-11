n = int(input("Enter n: "))
e = int(input("Enter e: "))
num = list(map(int, input("Enter c: ").split()))
m = int(input("Enter totient: "))

#Get D
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d = int(modinv(e, m))

for c in num:
  print(pow(c,d,n))
