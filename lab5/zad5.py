import keyword

slowa = ["for", "print", "break", "done", "bad"]

print("Czy słowo jest kluczowe w Pythonie?")
for slowo in slowa:
    czy_kluczowe = keyword.iskeyword(slowo)
    print(f"{slowo}: {czy_kluczowe}")