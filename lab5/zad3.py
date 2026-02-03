import time

def sekundnik(czas):
    while czas > 0:
        print("Pozostało sekund:", czas)
        time.sleep(1)
        czas -= 1
    print("Koniec czasu!")
sekundnik(10)