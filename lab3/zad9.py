while True:
    wiek_input = input("Podaj swój wiek: ")

    if not wiek_input.isdigit():
        print(" Błąd: wiek musi być liczbą całkowitą. Spróbuj ponownie.\n")
        continue

    wiek = int(wiek_input)

    if wiek < 0 or wiek > 130:
        print(" Błąd: podany wiek jest poza realistycznym zakresem (0–130). Spróbuj ponownie.\n")
        continue

    if wiek < 4:
        cena = 0
        print(" Wstęp bezpłatny (dziecko poniżej 4 roku życia).")

    elif wiek <= 17:
        cena = 10
        print(" Cena biletu dla dziecka: 10 zł.")

    else:
        student = input("Czy jesteś studentem? (tak/nie): ").strip().lower()

        if student == "tak":
            cena = 20 * 0.75
            print(" Cena biletu dla studenta: 15 zł (zniżka 25%).")
        else:
            cena = 20
            print(" Cena biletu dla dorosłego: 20 zł.")

    print(f"\n Do zapłaty: {cena:.2f} zł")
    break
