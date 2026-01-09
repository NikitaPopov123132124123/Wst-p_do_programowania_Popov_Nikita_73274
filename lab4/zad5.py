def srednia(lista):
    if len(lista) == 0:
        return 0  # lub można zwrócić komunikat o błędzie
    return sum(lista) / len(lista)

moje_liczby = [4, 7, 2, 9, 6]
wynik = srednia(moje_liczby)
print("Średnia wynosi:", wynik)
