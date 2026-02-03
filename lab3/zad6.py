droga = float(input("Podaj pokonaną drogę w kilometrach: "))
spalanie = float(input("Podaj średnie spalanie w litrach na 100 km: "))

cena_paliwa = 6.5

zuzycie = (droga / 100) * spalanie
koszt = zuzycie * cena_paliwa

print(f"\nPrzewidywane zużycie paliwa: {zuzycie:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")
