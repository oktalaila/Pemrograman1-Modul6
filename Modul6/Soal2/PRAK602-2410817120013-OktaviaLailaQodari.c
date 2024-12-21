#include <stdio.h>

int main() {
    int jumlah_ruangan;
    scanf("%d", &jumlah_ruangan);

    int angka[jumlah_ruangan];
    int hasil[jumlah_ruangan];

    for (int i = 0; i < jumlah_ruangan; i++) {
        scanf("%d", &angka[i]);
    }

    for (int i = 0; i < jumlah_ruangan; i++) {
        hasil[i] = angka[i] * (i + 1);
    }

    for (int i = 0; i < jumlah_ruangan; i++) {
        printf("%d ", hasil[i]);
    }
    printf("\n");

    return 0;
}