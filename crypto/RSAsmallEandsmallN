#Solves an RSA problem with small e and small n

import binascii
import gmpy
from gmpy import mpz

originalN = raw_input("n: ")
totientN = raw_input("totient of n: ")
eVal = raw_input("e: ")
cipherT = raw_input("c: ")

dVal = gmpy.invert(mpz(eVal), mpz(totientN))

finalVal = pow(mpz(cipherT), mpz(dVal), mpz(originalN))

hexMe = hex(finalVal)
print("go online and convert hex to ascii: ")
print(binascii.unhexlify(hexMe))
