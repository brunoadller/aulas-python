Lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Bolivia ', 'Colombia', 'Equador']

for pais in Lista:
    if pais == 'Uruguai':
        print("O pais é bicampeão Mundial!")
        for i in range(10):
            print(i)


for loop in range(0,len(Lista),2):
    print(Lista[loop])