#16. MANIPULANDO LISTAS
#AS LISTAS SÃO USADAS PARA ARMAZENAR CÁRIOS ITENS EM UMA ÚNICA VARIÁVEL
# AS LISTAS SÃO UM DOS QUATRO TIPOS DE DAODS INTERNOS DO PYTHON USADOS PARA ARMAZENAR COLEÇÕES DE DADOS, OS OUTROS 3 SÃO TUPLE
#SET E DICIONARY, TODOS COM QUALIDADE E USOS DIFERENTES

#COMANDOS MAIS UTILIZADOS:
#1.APPEND() ADICIONA NO FINAL DA LISTA
#2.LEN() CALCULAR O TAMANHO DA LISTA
#3.[] ACESSAR POSIÇÃO
#4.DEL() EXCLUIR ELEMENTO
#5.CLEAR() LIMPAR A LISTA
#6.INSERT() PARA INSERIR UM ITEM DE LISTA E UM INDICE ESPECIFICADO
#7.EXTEND() ANEXAR ELEMENTOS DE OUTROA LISTA À LISTA ATUAL
#8.REMOVE() REMOVE O ITEM ESPECIFICADO
#9.POP() REMOVE O ÍNDICE ESPECIFICADO
#10.SORT() ORDENAR OS VALORES
#11.COPY() FAZ UMA COPIA DA LISTA
#12. INDEX() RETORNA O INDEX DE ELEMENTO DA LISTA
"""

lista_vazia = []
print(lista_vazia)

lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)

print(lista_vazia)
print(len(lista_vazia))
print(lista_vazia[2])
print(lista_vazia[0:2])
lista_vazia.clear()
print(lista_vazia)
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)


print(lista_vazia)
lista_vazia.insert(0, '0')
print(lista_vazia) 
lista_vazia.insert(3, "bruno")
print(lista_vazia)

lista1 = [0,1,2,3]
lista2 = [4,5,6,7]
lista1.extend(lista2)

print(lista1)
lista1.remove(5)
print(lista1)
lista1.pop(0)
print(lista1)
lista_ABC = ['A', 'B', 'Z','M','Y']
lista_ABC.sort(reverse=True)
print(lista_ABC)
listanova = lista_ABC.copy()
print(listanova)
print(lista_ABC.index('M'))

banco_de_dados = [
    {"nome": "Ana Silva", "idade": 25, "telefone": "11987654321"},
    {"nome": "Bruno Costa", "idade": 32, "telefone": "21999887766"},
    {"nome": "Carlos Souza", "idade": 41, "telefone": "31988776655"},
    {"nome": "Daniela Lima", "idade": 28, "telefone": "41977665544"},
    {"nome": "Eduardo Alves", "idade": 36, "telefone": "51966554433"},
    {"nome": "Fernanda Torres", "idade": 22, "telefone": "61955443322"},
    {"nome": "Gabriel Rocha", "idade": 30, "telefone": "71944332211"},
    {"nome": "Helena Martins", "idade": 27, "telefone": "81933221100"},
    {"nome": "Igor Fernandes", "idade": 35, "telefone": "11911112222"},
    {"nome": "Juliana Ribeiro", "idade": 29, "telefone": "21922223333"},
    {"nome": "Kleber Moreira", "idade": 40, "telefone": "31933334444"},
    {"nome": "Larissa Mendes", "idade": 24, "telefone": "41944445555"},
    {"nome": "Marcos Oliveira", "idade": 31, "telefone": "51955556666"},
    {"nome": "Natália Barros", "idade": 26, "telefone": "61966667777"},
    {"nome": "Otávio Pires", "idade": 38, "telefone": "71977778888"},
    {"nome": "Patrícia Castro", "idade": 34, "telefone": "81988889999"},
    {"nome": "Rafael Santos", "idade": 23, "telefone": "11900001111"},
    {"nome": "Sabrina Nunes", "idade": 28, "telefone": "21911112222"},
    {"nome": "Thiago Azevedo", "idade": 37, "telefone": "31922223333"},
    {"nome": "Vanessa Duarte", "idade": 33, "telefone": "41933334444"}
]

print(banco_de_dados)
banco_de_dados.insert(0, {"nome": "Juliano fonseca", "idade": 19, "telefone": "41933334444"})
print(banco_de_dados)
banco_de_dados.pop(2)
print(banco_de_dados)
"""

banco_de_dados = [
    {"nome": "Ana Silva", "idade": 25, "telefone": "11987654321"},
    {"nome": "Bruno Costa", "idade": 32, "telefone": "21999887766"},
    {"nome": "Carlos Souza", "idade": 41, "telefone": "31988776655"},
    {"nome": "Daniela Lima", "idade": 28, "telefone": "41977665544"},
    {"nome": "Eduardo Alves", "idade": 36, "telefone": "51966554433"},
    {"nome": "Fernanda Torres", "idade": 22, "telefone": "61955443322"},
    {"nome": "Gabriel Rocha", "idade": 30, "telefone": "71944332211"},
    {"nome": "Helena Martins", "idade": 27, "telefone": "81933221100"},
    {"nome": "Igor Fernandes", "idade": 35, "telefone": "11911112222"},
    {"nome": "Juliana Ribeiro", "idade": 29, "telefone": "21922223333"},
    {"nome": "Kleber Moreira", "idade": 40, "telefone": "31933334444"},
    {"nome": "Larissa Mendes", "idade": 24, "telefone": "41944445555"},
    {"nome": "Marcos Oliveira", "idade": 31, "telefone": "51955556666"},
    {"nome": "Natália Barros", "idade": 26, "telefone": "61966667777"},
    {"nome": "Otávio Pires", "idade": 38, "telefone": "71977778888"},
    {"nome": "Patrícia Castro", "idade": 34, "telefone": "81988889999"},
    {"nome": "Rafael Santos", "idade": 23, "telefone": "11900001111"},
    {"nome": "Sabrina Nunes", "idade": 28, "telefone": "21911112222"},
    {"nome": "Thiago Azevedo", "idade": 37, "telefone": "31922223333"},
    {"nome": "Vanessa Duarte", "idade": 33, "telefone": "41933334444"}
]


print("Informe o indereço do aluno que deseja remover: ")
aluno = int(input("Endereco: "))
print(banco_de_dados)
banco_de_dados.pop(aluno)

print(banco_de_dados)
banco_de_dados.sort(reverse=True)
print(banco_de_dados)
