# A=65
# Z=91

r = 5
c = 0

for i in range(r):
    for j in range(r - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()

print()
# for reverse

for i in reversed(range(r)):
    for j in range(r - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()
print()
# for diamont

for i in range(r):
    for j in range(r - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()


for i in reversed(range(r)):
    for j in range(r - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()