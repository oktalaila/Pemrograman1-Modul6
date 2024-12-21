baris, kolom = map(int, input().split())
angka = []
x = 0
matriks = list(map(int, input().split()))
for i in range(baris):
    angka.append(matriks[x:x+kolom])
    x = x + kolom
for baris in angka:
    for value in baris:
        print(value, end=' ')
    print()