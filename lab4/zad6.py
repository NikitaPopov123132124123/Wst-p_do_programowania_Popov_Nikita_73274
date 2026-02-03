def info(imie, wiek=20):
    """Funkcja wypisuje imię oraz wiek użytkownika."""

    print("Imię:", imie)
    print("Wiek:", wiek)


print(info.__doc__)

info("Michał", 17)
info("Ola")  # brak argumentu 'wiek' → użyje wartości domyślnej 20
