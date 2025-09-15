

#o exemplo dado, no qual atribuímos a variável 
#"nome" o valor de "Guido", "G" ocupa a posição 0 na sequência,
#"u" ocupa a posição 1, "i" a posição 2, e assim por diante. 
#A função enumerate() recebe como parâmetro 
#a sequência e retorna a posição.


#nome = 'Guido'
#for i, c in enumerate(nome):
#    print(f"Posição = {i}, valor = {c}")
    
#Para criar uma sequência numérica de iteração em Python,
#podemos usar a função range()

#for x in range(5):
#  print(x)


#for i in range(0,5):
#   print(i)

#incrementrador será o terceiro parâmetro
for i in range(10, 20, 2):
    print(i)