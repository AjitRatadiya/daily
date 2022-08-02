
r = 5
c = 0

for i in range(r):
    for j in range(r):
        print(chr(65+c), end=' ')
        c += 1
    print()