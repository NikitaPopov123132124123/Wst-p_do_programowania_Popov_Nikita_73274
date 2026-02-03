#Sposób 1
import f_mat

wynik_1a = f_mat.kwadrat(10)
wynik_1b = f_mat.szescian(3)
wynik_1c = f_mat.dodaj(10, 5)

print("--- Sposób 1 ---")
print(f"Kwadrat 10: {wynik_1a}")
print(f"Sześcian 3: {wynik_1b}")
print(f"Suma 10+5: {wynik_1c}")

#Sposób 2
from f_mat import kwadrat, szescian, dodaj

wynik_2a = kwadrat(10)
wynik_2b = szescian(3)
wynik_2c = dodaj(10, 5)

print("\n--- Sposób 2 ---")
print(f"Kwadrat 10: {wynik_2a}")
print(f"Sześcian 3: {wynik_2b}")
print(f"Suma 10+5: {wynik_2c}")