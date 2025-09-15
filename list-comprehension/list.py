

linguagens = '''Python Java javascript C C# C++ Swift Go Kotlin'''.split()

print("Antes da Listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()
    
print("\nDepois da listcomp = ", linguagens)


#UTILIZANDO LIST COMP
linguagens2 = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = [item for item in linguagens2 if "Java" in item]


print(linguagens_java)

#PARA VERIFICAR SE FOR INDÊNTICO
linguagens_java2 = [item for item in linguagens2 if "Java" == item]


print(linguagens_java2)


