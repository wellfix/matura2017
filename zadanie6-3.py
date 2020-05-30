plik = open("dane.txt").read().split("\n")
for i, x in enumerate(plik):
    plik[i] = plik[i].split()
for i in range(200):
    for j in range(320):
        plik[i][j]=int(plik[i][j])
sum = 0
somsiad = 0
for p in range(200):
    for q in range(320):
       sum = 0
       if p > 0 and abs(plik[p][q] - plik[p-1][q]) > 128:
           sum = 1
       if p < 199 and abs(plik[p][q] - plik[p + 1][q]) > 128:
           sum = 1
       if q > 0 and abs(plik[p][q] - plik[p][q-1]) > 128:
           sum = 1
       if q < 319 and abs(plik[p][q] - plik[p][q+1]) > 128:
           sum = 1
       somsiad += sum
print(somsiad)
