#===============================zad6============================================




# numer a
# for i in range(10):
#    print(i)
# numer a ver 2
# for i in range(10):
#    print(i+1)

# numer b
# for i in range(10, -1,-1):
#    print(i+1)

# numer c
# for i in range(77, 1, -7):
#    print(i)

# numer d
#for i in range(20, -1, -2):
#    print(i)



#==========================zad7=================================







#A
#n= int(input("podaj co-to-tam: "))
#for j in range(n): # wiersze
#    for i in range(n): # qwiazdki w wiersze
#        print("* ", end="")
#    print("")


#B
#n= int(input("podaj co-to-tam: "))
#for j in range(n):
#    for i in range(n-(n-j-1)):
#        print("* ", end="")
#    print("")


#C
#n= int(input("podaj co-to-tam: "))
#for j in range(n):
#    for i in range(n-(n-j-1)):
#        print("* ", end="")
#    print("")


#==================================zad8==================================

#x = -4 # koniec gdy x=4
#
#while x<=4:
#    print(x)
#    y = 2* x**2 -5 *x -8
#    print(f"dla x ruvnego {x} wartosc co-go-to-tam")
#    x += 0.5 #x = x+0.5


#==================================zad9===================================

while True:
    a = int(input("Podaj zakaz liczbe: "))
    if a<0:
        break

