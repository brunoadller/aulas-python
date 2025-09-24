Lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Bolivia ', 'Colombia', 'Equador']

x = 0
#tentar usar enumerate()
for index, pais in enumerate(Lista):
    print(x, pais)
    x+= 1  


lista = [Numero ** 2 for Numero in range(0,10,2)]
print(lista)


lista2 = []
for loop in range(0,10):
    lista2.append(loop)

print(lista2)