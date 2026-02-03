import random

import math

try:
    start = int(input("Podaj początek zakresu losowania: "))
    end = int(input("Podaj koniec zakresu losowania: "))

    wylosowane = tuple(random.randint(start, end) for _ in range(10))
    print(f"Wylosowana krotka: {wylosowane}")

    iloczyn = 1
    for liczba in wylosowane:
        iloczyn *= liczba

    srednia_geo = iloczyn ** (1 / 10)


    print(f"Średnia geometryczna: {srednia_geo:.4f}")

except ValueError:
    print("Proszę podać poprawne liczby całkowite.")