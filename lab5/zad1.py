#a
import random

szczesliwy_numerek = random.randint(1, 30)
print("Szczęśliwy numerek:", szczesliwy_numerek)

#b
import random

roczniki = [2004, 2005, 2004, 2006, 2005, 2004, 2006]
szczesliwy_rocznik = random.choice(roczniki)

print("Szczęśliwy rocznik:", szczesliwy_rocznik)

#c
import random

liczby = list(range(1, 50))
losowanie = random.sample(liczby, 6)

print("Wylosowane liczby Lotto:", sorted(losowanie))