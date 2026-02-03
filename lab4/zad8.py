def potega(a, n):
    # przypadek bazowy
    if n == 0:
        return 1
    # rekurencja
    return a * potega(a, n - 1)

print(potega(2, 5))   # 2^5 = 32
