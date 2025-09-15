#6º TIPO DE INFORMAÇÃO

#1 - Text Type: str
#2 - Numeric Types: int, float, compelx
#3 - Sequences Types: list, tuple, range
#4 - Mapping Type: dict
#5 - Set Type: set, frozenset
#6 - Boolean Type: bool
#7 - Binary Types: bytes, bytearray, memoryview


string = str("olá mundo")
inteiro = int(10)
flutuante = float(100.5)
complex = complex(10)
lista = list(('Maça', 'Morango'))
tupla = tuple(('A', 'B'))
Range = range(6)
dicionario = dict(nome='odemir', age=29)
set=set(('A', 'B', 'C'))
fronzet = frozenset(('A', 'B', 'C'))
Boleano = bool(5)
Bytes = bytes(5)
byteArray = bytearray(5)
Menoryview = memoryview(bytes(5))

from datetime import datetime
Data = datetime.today().date()


print(type(Data))