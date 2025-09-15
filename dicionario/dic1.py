dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 30

dici_2 = {'nome':'João', 'idade': 30}

dici_3 = dict([('nome', 'João'), ('idade', 3)])

dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))

print(dici_1 == dici_2 == dici_3 == dici_4)