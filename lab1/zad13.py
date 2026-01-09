a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("\nWybierz działanie:")
print("1. Dodawanie (+)")
print("2. Odejmowanie (-)")
print("3. Mnożenie (*)")
print("4. Dzielenie (/)")
operacja = input("Podaj symbol operacji (+, -, *, /): ")

if operacja == "+":
    wynik = a + b
    print(f"\n Wynik: {a} + {b} = {wynik}")

elif operacja == "-":
    wynik = a - b
    print(f"\n Wynik: {a} - {b} = {wynik}")

elif operacja == "*":
    wynik = a * b
    print(f"\n Wynik: {a} * {b} = {wynik}")

elif operacja == "/":
    if b != 0:
        wynik = a / b
        print(f"\n Wynik: {a} / {b} = {wynik}")
    else:
        print("\n Błąd: nie można dzielić przez zero!")

else:
    print("\n Nieznane działanie! Użyj jednego z symboli: +, -, *, /.")


# --- KOMENTARZ ---
# W Pythonie NIE istnieje instrukcja 'switch' znana z innych języków (np. C, Java, C++).
# Zamiast niej stosuje wielokrotne 'elif', które działa podobnie:
# sprawdza kolejne warunki i wykonuje kod pierwszego pasującego przypadku.
#
# Od wersji Python 3.10 można używać nowej konstrukcji 'match-case',
# która jest bardzo podobna do 'switch':
#
# match operacja:
#     case "+":
#         wynik = a + b
#     case "-":
#         wynik = a - b
#     ...
#
# Jednak w tym zadaniu wykorzystalem klasyczne 'if / elif / else',
# aby zachować kompatybilność ze starszymi wersjami Pythona.
