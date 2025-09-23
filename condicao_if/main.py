#Condição, se a pessoa tiver menos de 18 anos, ela não entra no sistema
Idade = 15

if Idade >= 18:
    print("Você é maior de idade!!")
elif Idade >= 15 and Idade <= 17:
    print("Pai ou mãe podem autorizar!!")
else:
    print('Você é menor de idade!!')