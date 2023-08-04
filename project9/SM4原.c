#include "SM4.h"




#include "SM4.h"
#include <stdint.h>



void R(uint32_t* input, uint32_t* output) {
    output[0] = input[3];
    output[1] = input[2];
    output[2] = input[1];
    output[3] = input[0];
}

void keyExpansion(const uint32_t* MK, uint32_t* RK) {
    uint32_t K[36];
    uint32_t i, j;

    for (i = 0; i < 4; i++) K[i] = MK[i] ^ CK[i];

    uint32_t tmp1, tmp2, tmp3;
    uint8_t a[4];
    uint8_t b[4];
    for (i = 0; i < 32; i++) {
        tmp1 = K[i + 1] ^ K[i + 2] ^ K[i + 3] ^ CK[i];

        // 32b -> 8b
        for (j = 0; j < 4; j++) {
            a[3 - j] = tmp1 & 0xff;
            tmp1 >>= 8;
        }
        // Sbox
        for (j = 0; j < 4; j++) {
            uint8_t x = (a[j] >> 4) & 0xf;
            uint8_t y = a[j] & 0xf;
            b[j] = Sbox[x][y];
        }
        // 8b -> 32b
        tmp2 = b[0] | (uint32_t)b[1] << 8 | (uint32_t)b[2] << 16 | (uint32_t)b[3] << 24;
        // L'
        tmp3 = tmp2 ^ (tmp2 << 13 | tmp2 >> 19) ^ (tmp2 << 23 | tmp2 >> 9);

        K[i + 4] = K[i] ^ tmp3;
        RK[i] = K[i + 4];
    }
}

void SM4_Encrypt(const uint32_t* MK, const uint32_t* PT, uint32_t* CT) {
    uint32_t RK[32];
    keyExpansion(MK, RK);

    uint32_t X[36];
    uint32_t i, j, tmp1, tmp2, tmp3;

    for (i = 0; i < 4; i++) X[i] = PT[i];

    uint8_t a[4];
    uint8_t b[4];
    for (i = 0; i < 32; i++) {
        tmp1 = X[i + 1] ^ X[i + 2] ^ X[i + 3] ^ RK[i];

        // 32b -> 8b
        for (j = 0; j < 4; j++) {
            a[3 - j] = tmp1 & 0xff;
            tmp1 >>= 8;
        }
        // Sbox
        for (j = 0; j < 4; j++) {
            uint8_t x = (a[j] >> 4) & 0xf;
            uint8_t y = a[j] & 0xf;
            b[j] = Sbox[x][y];
        }
        // 8b -> 32b
        tmp2 = b[0] | (uint32_t)b[1] << 8 | (uint32_t)b[2] << 16 | (uint32_t)b[3] << 24;
        // L
        tmp3 = tmp2 ^ (tmp2 << 2 | tmp2 >> 30) ^ (tmp2 << 10 | tmp2 >> 22) ^ (tmp2 << 18 | tmp2 >> 14) ^ (tmp2 << 24 | tmp2 >> 8);

        X[i + 4] = X[i] ^ tmp3;
    }

    uint32_t Y[4];
    for (i = 0; i < 4; i++) Y[i] = X[i + 32];

    R(Y, CT);
}



