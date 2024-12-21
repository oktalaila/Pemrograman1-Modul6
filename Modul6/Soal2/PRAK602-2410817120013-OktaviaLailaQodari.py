def main():
    jumlah_ruangan = int(input())
    angka = list(map(int, input().split()))
    
    hasil = []
    for i in range(jumlah_ruangan):
        jumlah = angka[i] * (i + 1)
        hasil.append(jumlah)
    
    print(" ".join(map(str, hasil)))

main()