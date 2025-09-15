#10 MANIPULANDO STRINGS


#1.replace()
#2.startswith()
#3.endswith()
#4.count()
#5.capitalize()
#6.isdigit()
#7.isalnum()
#8.upper()
#9.lower()
#10.find()
#11.strip()
#12.split()


string = 'Bruno Adller Martinez'
cpf = 'CPF:03951572000'
print(string)
print(len(string))
print(type(string))
print(string + ' concantenar')
#replace(substituir)
print(string.replace('Martinez', 'Fonseca'))
print(int(cpf.replace('CPF:', '')))
#startswith() (começa com) #endswith(termina com)
print(string.startswith('Bruno')) #retorna booleano se for verdadeiro ou falso
print(string.endswith('Martinez'))
#count() contar palavras ou letras
print(string.count('Bruno'))
nome = "bruno adller"
print(nome.capitalize())
#isdigit() verificra se existe

string_CPF = '1234567891'
print(string_CPF.isdigit())
#verifica se é alpha numérico
print(string.isalnum())
#upper maiúscula lower minuscula

print(string.upper())
print(string.lower())

Frase = " Hoje o dia está calor !!!!  "

print(Frase.find('asasasa'))#-1 se não existe posição onde começa se existir

#strip() remove espações entre o fim e começo das palavras

print(Frase.strip())

#split() quebrar as string

palavra = "Rua Augusta 250, Centro, SP"
print(palavra.split(','))