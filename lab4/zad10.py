def hanoi(n, start, pomocniczy, cel):
    # jeśli jest tylko jeden krążek – przenieś go bezpośrednio
    if n == 1:
        print(f"Przenieś krążek z {start} na {cel}")
        return

    # 1. Przenieś n-1 krążków na wieżę pomocniczą
    hanoi(n - 1, start, cel, pomocniczy)

    # 2. Przenieś największy krążek
    print(f"Przenieś krążek z {start} na {cel}")

    # 3. Przenieś n-1 krążków z powrotem na wieżę końcową
    hanoi(n - 1, pomocniczy, start, cel)


hanoi(3, "A", "B", "C")
