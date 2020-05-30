plik = open("dane.txt").read().split("\n")
for i, x in enumerate(plik):
    plik[i] = plik[i].split()
for i in range(200):
    for j in range(320):
        plik[i][j]=int(plik[i][j])
prosta = 0

for x in range(320):
    sum = 1
    for y in range(199):
        if plik[y][x] == plik[y+1][x]:
            sum+=1
        elif sum > 1 and plik[y][x] != plik[y+1][x]:
            sum = 1
        if sum > prosta:
            prosta = sum
print(prosta)