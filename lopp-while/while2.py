import random

while True:
    eu = random.randint(0,3)
    contra_voces = random.randint(2,10)

    print("Eu tirei o valor: ",eu)
    print("Voces tiraram o valor: ", contra_voces)

    if(eu > contra_voces):
        print("Ganhei !!!!!!!")
        break
   
    print('\n')