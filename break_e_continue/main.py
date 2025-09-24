

lista = ['Banana', 'Morango', 'Pera', 'Uva', 'Abacaxi']

for fruta in lista:
    print(fruta)
    if(fruta == 'Uva'):
        break


for loop in range(0,11):
    if(loop == 5):
        continue
        print('Chegue aqui, mas vou ser ignorado!!')
    print(loop)