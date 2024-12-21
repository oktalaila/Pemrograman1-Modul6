x = 0
y = 0

kode = input()
pesan = input()

if len(kode) != len(pesan):
    print("Panjang kalimat berbeda, pesan palsu")
else:
    for i in range(len(kode)):
        if kode[i] == " " and pesan[i] == " ":
            print(end=" ")
            
        elif kode[i] == pesan[i]:
            print("*", end="")
            x += 1
        else:
            print("#", end="")
            y += 1

    print("\n* =", x)
    print("# =", y)

    if x >= y:
        print("Pesan Asli")
    else:
        print("Pesan Palsu")