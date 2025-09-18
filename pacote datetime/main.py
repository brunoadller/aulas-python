#17 Pacote externo datetime
#fornece classes para manipular data e hora


import datetime

dia_hoje = datetime.datetime.today()
print(dia_hoje)

print(type(dia_hoje))

print(dia_hoje.date())

Data = datetime.datetime.today().date()

Ano = Data.year
Mes = Data.month
Dia = Data.day

print(Ano, Mes, Dia)


Data_antiga = datetime.date(1997,12,2)
print(type(Data_antiga))

print(Data.strftime('%d/%m/%y'))

print(Data)
print(Data + datetime.timedelta(days=30))