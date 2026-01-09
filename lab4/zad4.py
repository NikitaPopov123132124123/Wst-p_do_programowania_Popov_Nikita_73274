def oblicz_bmi(waga, wzrost):
    # wzrost podajemy w metrach, np. 1.75
    bmi = waga / (wzrost ** 2)
    print("Twoje BMI wynosi:", round(bmi, 2))

    if bmi < 18.5:
        print("Zakres: niedowaga.")
    elif bmi < 25:
        print("Zakres: prawidłowa masa ciała.")
    elif bmi < 30:
        print("Zakres: nadwaga.")
    else:
        print("Zakres: otyłość.")

    return bmi

oblicz_bmi(70, 1.75)
