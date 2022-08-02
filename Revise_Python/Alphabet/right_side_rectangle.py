# A=65
# Z=91

ran = 5
count = 0

for i in range(ran):
    for j in range(1, ran-i):
        print(" ", end=' ')
    for k in range(i+1):
        print(chr(65+k), end=' ')
    print()
