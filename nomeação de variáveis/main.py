#NOMEAÇÃO DE VARIÁVEIS
#1 - Declarar as variáveis em uma única linha de comando
#2- Atribuir um valor à diversas variáveis
#3 - Declarar usando uma Lista
#4 - Combinar variáveis
#5 - operadores matemáticos
#6 - Muitos outros

#Nomenado
Laranja, Melao, limao = 1,2,3

Morango = uva = kiwi = 100
print(Morango, uva, kiwi)


#Nomear com listas
lista_carros = ['VW', 'Audi', 'Tesla']
Marca_01, Marca_02, Marca_03 = lista_carros
print(Marca_01, Marca_02, Marca_03)

#combinar variáveis
Nome = 'odemir'
Sobrenome = 'Depieri'

Nome_completo = Nome +' '+Sobrenome

print(Nome_completo)

#experimento
Nome = 'Odemir'
Idade = 29

print(Nome + str(Idade))

Investimento = 1000
taxa_juros = float('0.2')
print(Investimento * taxa_juros)
valor_ganhado = (Investimento * taxa_juros) * Investimento

print(valor_ganhado)