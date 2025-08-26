input = 'Working'
encrypted = ''

for x in input:
   encrypted = encrypted + chr(ord(x) +1)

print(encrypted)