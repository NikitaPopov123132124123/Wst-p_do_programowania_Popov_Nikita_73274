while True:
    wiek_input = input("Podaj swój wiek: ")

    if not wiek_input.isdigit():
        print("Błąd: wiek musi być liczbą całkowitą. Spróbuj ponownie.\n")
        continue

    wiek = int(wiek_input)

    if wiek < 0 or wiek > 130:
        print("Błąd: podany wiek jest poza realistycznym zakresem (0–130). Spróbuj ponownie.\n")
        continue

    if wiek >= 18:
        print("Jesteś pełnoletni/a.")
    else:
        print("Nie jesteś jeszcze pełnoletni/a.")
    break
