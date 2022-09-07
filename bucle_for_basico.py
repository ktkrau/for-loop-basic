#1. Imprime todos los números enteros del 0 al 150
for x in range(0,151):
    print(x)

#2.Imprime todos los múltiplos de 5 entre 5 y 1000

for a in range(5,1001):
    if a % 5 == 0:
        print(a)

#3.Imprime números enteros del 1 al 100. si es divisible por 5, imprime "Coding" en su lugar.
#Si es divisible por 10, imprime "Coding Dojo".

for b in range(1,101):
    if b % 10 == 0:
        print("Coding Dojo")
    elif b % 5 == 0:
        print("Coding")
    else: 
        print(b)

#4.Agrega los enteros impares del 0 al 500.000 e imprime la suma final
suma = 0
for c in range(0,500001):
    if c % 2 != 0:
        print(c)
        suma += c
print(suma)

#5.Imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4

inicio = 2018

while inicio>=0:
    print(inicio)
    inicio = inicio -4

#6.Establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando
# por highNum, imprime solo los enteros que sean múltiplos de mult.

lowNum = 2
highNum = 9 
mult = 3

for e in range(lowNum, highNum+1):
    if e % 3 == 0:
        print(e)
