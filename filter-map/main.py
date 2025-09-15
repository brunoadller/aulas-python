print("Exemplo 1")
linguagens = '''Python Java Javascript C C# C++ Swift Go Kotlin'''.split()

#A função map só funciona se converter para uma lista
nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}\n")


nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")


#exemplo2
print("\n\nExemplo 2")

numeros = [0,1,2,3,4,5]

quadrados = list(map(lambda x: x*x, numeros))

print(f"Lista com número eleveado a ele mesmo = {quadrados}")