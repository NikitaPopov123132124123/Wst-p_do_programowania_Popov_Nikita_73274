import math

print("Program rozwiązuje równanie kwadratowe: a*x^2 + b*x + c = 0\n")

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie tożsamościowe – nieskończenie wiele rozwiązań.")
        else:
            print("Równanie sprzeczne – brak rozwiązań.")
    else:
        x = -c / b
        print(f"To nie jest równanie kwadratowe. Rozwiązanie liniowe: x = {x:.2f}")
else:
    delta = b**2 - 4*a*c
    print(f"\nDelta = {delta:.2f}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Równanie ma dwa pierwiastki rzeczywiste:")
        print(f"x₁ = {x1:.2f}")
        print(f"x₂ = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Równanie ma jeden pierwiastek podwójny:")
        print(f"x = {x:.2f}")
    else:
        print("Równanie nie ma rozwiązań rzeczywistych (Δ < 0).")
