from datetime import datetime

def terminarz():
    dzisiaj = datetime.now()

    ostatnie_lab = datetime(2025, 12, 16)  # Przykładowa data
    kolokwium = datetime(2026, 1, 27)  # Przykładowa data

    dni_od_lab = (dzisiaj - ostatnie_lab).days
    czas_do_kolokwium = kolokwium - dzisiaj

    miesiac = kolokwium.strftime("%B")

    print(f"Od ostatnich laboratoriów minęło: {dni_od_lab} dni.")
    print(f"Do kolokwium w miesiącu {miesiac} zostało: {czas_do_kolokwium.days} dni.")


terminarz()