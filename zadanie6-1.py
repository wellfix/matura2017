plik = open("dane.txt").read().split()

for i, x in enumerate(plik):
    plik[i] = int(x)
zadanie  = sorted(plik)
print(zadanie[0])
print(zadanie[63999])