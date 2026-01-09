import random
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100 km): "))
droga = random.randint(50, 1000)
zuzycie_paliwa = (droga * srednie_spalanie) / 100
koszt_podrozy = zuzycie_paliwa * 6.5
print(f"\nDługość trasy: {droga} km")
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")
