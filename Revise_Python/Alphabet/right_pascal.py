r = 5
c = 0

for i in range(r):
    for j in range(i+1):
        print(chr(65+j), end='')
    print()
for i in reversed(range(r)):
    for j in range(i):
        print(chr(65+j), end='')
    print()
