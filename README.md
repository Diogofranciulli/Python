# Python 

a = 4
b = -20
c = 24

delta = (b**2) - (4 * a * c)

x1 = (- b + (delta** 0.5))/ (2 * a)

x2 = (- b - (delta ** 0.5))/ (2 * a)

print("as raizes são" ,x1, "e" , x2)


a = 1.500

promocao = (15/100) * a

final = a + promocao

print("O aumento de 15 % no final é de " , final)


a1 = 10

a1, b1 = 3 *a1 , a1

print(a1, b1)

#colocar a em b e b em a
# metodo nao recomendado
a2 = 10
b2 = 20

a2, b2 = b2 , a2
print(a2, b2)

#metodo recomendado

a3 = 45
b3 = 30
aux = a3
a3 = b3
b3 = aux
print(a3, b3)

# 1 hora = 60 minutos ; 60 minutos = 3600 segundos ; 1 minuto = 60 segundos

tempo = int(input("Digite o numero que quer converter em horas, minutos e segundos"))
minuto = tempo// 60 % 60
hora = tempo//3600
segundos = tempo % 60
print(minuto, "minutos" , hora , "horas" , segundos , "segundos")

