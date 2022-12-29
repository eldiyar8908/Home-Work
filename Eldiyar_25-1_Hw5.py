data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
i = 0
operators = {}
print(len(operators))
while len(operators) != len(designations):
    operators[designations[i]] = {codes[i]}
    i += 1
del operators['Fonex']
del operators['Katel']
operators['O!'].add('0700')
operators['O!'].add('0500')
operators['Megacom'].add('0999')
operators['Megacom'].add('0555')
operators['Beeline'].add('0222')
operators['Beeline'].add('0777')
for key,value in operators.items():
    print(f'{key} - {value}')

