import time


print("comecei agora....")
time.sleep(3)
print("Terminei agora...")


Agora = time.localtime()

print(Agora)
print(type(Agora))


print(time.strftime("%d/%m/%y, %H:%M:%S", Agora ))

time_texto = '21 June, 2021'
print(time.strptime(time_texto, '%d %B, %Y'))