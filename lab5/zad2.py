import math
import cmath

#a
wynik_a = math.sqrt(81)
print(f"a) sqrt(81) = {wynik_a}")

#b
wynik_b = math.pow(8, 10)
print(f"b) 8^10 = {wynik_b}")

#c
wynik_c = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
print(f"c) sqrt(2) + sqrt(3) + sqrt(6) = {wynik_c}")

#d
#używamy cmath dla liczb zespolonych:
wynik_d = cmath.sqrt(-5)
print(f"d) sqrt(-5) = {wynik_d}")

#e
# Można to zapisać jako potęgowanie: 125^(1/3)
wynik_e = math.pow(125, 1/3)
print(f"e) cbrt(125) = {wynik_e}")