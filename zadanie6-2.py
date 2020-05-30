plik = open("dane.txt").read().split("\n")
for i, x in enumerate(plik):
    plik[i] = plik[i].split()
row = 0
for x in range(200):
    for y in range(160):
        if plik[x][y] != plik[x][319-y]:
            row = row +1
            break
print(row)