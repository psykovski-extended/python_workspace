a = 10
bnr = bin(a).replace('0b', '')
x = bnr[::-1]
while len(x) < 4:
    x += '0'
bnr = x[::-1]
print(bnr)
