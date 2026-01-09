import math

def pole_trojkata(a, b, c):
    try:
        # sprawdzenie, czy wszystkie dane są liczbami dodatnimi
        if a <= 0 or b <= 0 or c <= 0:
            return "Boki muszą być dodatnie."

        # sprawdzenie nierówności trójkąta
        if a + b <= c or a + c <= b or b + c <= a:
            return "Z takich boków nie da się zbudować trójkąta."

        # wzór Herona
        p = (a + b + c) / 2
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return pole

    except TypeError:
        return "Podano niepoprawny typ danych."
    except Exception as e:
        return f"Wystąpił nieoczekiwany błąd: {e}"


print(pole_trojkata(3, 4, 5))      # poprawne dane
print(pole_trojkata(1, 2, 10))     # nie tworzy trójkąta
print(pole_trojkata(-3, 4, 5))     # błąd (ujemny bok)
print(pole_trojkata("a", 4, 5))    # błąd typu
