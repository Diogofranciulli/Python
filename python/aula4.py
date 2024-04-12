print("Boas vindas")
nome=input("nome?")
idade = int(input("ano de nascimento"))
end=input("endereço")
uva=10
laranja=12
banana=4
maca=5
kiwi=20

print("uva - 10")
print("laranja - 12")
print("banana - 4")
print("maçã - 5")
print("kiwi - 20")
fruta=input("qual fruta?")
peso = float(input("quantidade"))

if fruta=="uva":
    valor=peso*uva
elif fruta == "laranja":
    valor=peso*laranja
elif fruta == "banana":
    valor=peso*banana
elif fruta =="maca":
    valor=peso*maca
elif fruta=="kiwi":
    valor=peso*kiwi
else:
    print("escolha invalida")
print(valor)
frete=3
if valor<15:
    valor=valor+frete
else:
    print("isento de frete")

#print(valor)

if idade > 60:
    print("desconto de 5%")
    valor=valor*0.95
    print(valor)

print("valeu")
