import datetime

date = datetime.datetime.today()
data = date.date()
dia = data.day
mes = data.month
ano = data.year

result = f"{dia:02d}/{mes:02d}/{ano}"
print(result)