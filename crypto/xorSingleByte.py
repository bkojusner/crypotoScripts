import binascii
import re

w = open('output.txt','w+')

with open('input.txt') as f:
  for line in f:
    encoded = line.strip()
    nums = binascii.unhexlify(encoded)
    strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
    w.write(max(strings, key=lambda s: s.count(' ')))

w.close()

with open('output.txt') as i:
  for line in i:
    str = line
    x = re.search("^flag", str)
    if (x):
      print(str)
