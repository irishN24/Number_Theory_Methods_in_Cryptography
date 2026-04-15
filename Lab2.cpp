//Лабораторная работа №2. Дихотомический алгоритм возведения в степень.
static int bitLength(const Big_Number& num) {
    if (num.len == 1 && num.coef[0] == 0) return 0;
    int msbWord = num.len - 1;
    while (msbWord >= 0 && num.coef[msbWord] == 0) --msbWord;
    if (msbWord < 0) return 0;
    Base val = num.coef[msbWord];
    int bits = 0;
    while (val) { bits++; val >>= 1; }
    return msbWord * BASE_SIZE + bits;
}
static int getBit(const Big_Number& num, int pos) {
    if (pos < 0) return -1;
    int wordIdx = pos / BASE_SIZE;
    int bitIdx = pos % BASE_SIZE;
    if (wordIdx >= num.len) return 0;
    return (num.coef[wordIdx] >> bitIdx) & 1;
}
Big_Number Exponentiation_t(const Big_Number& exponent) const{
    int bits = bitLength(exponent);
    //cout << "bits: " << bits << endl;
    // a^0 = 1
    if (exponent.len == 1 && exponent.coef[0] == 0) {
        Big_Number res(1);
        res.coef[0] = 1;
        return res;
    }
    // a^1 = a
    if (exponent.len == 1 && exponent.coef[0] == 1) {
        return *this;
    }
    // 1^a = 1
    if (len == 1 && coef[0] == 1) {
        Big_Number res(1);
        res.coef[0] = 1;
        return res;
    }
    // 0^0 = 1
    if((len == 1 && coef[0] == 0) && (exponent.len == 1 && exponent.coef[0] == 0)){
        Big_Number res(1);
        res.coef[0] = 1;
        return res;
    }
    // 0^a = 0
    if (len == 1 && coef[0] == 0) {
        Big_Number res(1);
        res.coef[0] = 0;
        return res;
    }

    Big_Number z;
    z = 1;

    Big_Number q = *this;

    for (int i = 0; i < bits; ++i) {
        if (getBit(exponent, i) == 1) {
            z = z * q;
        }
        q = q.fast_square();
    }

    return z;
}
}
