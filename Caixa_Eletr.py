print('==='*15)
print('        BANCO FERROUSE   ')
print('==='*15)
saque = float(input('Qual o valor a ser sacado '))
total = saque
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totalced = 0
        if total == 0:
            break

print('==='*15)
print('O Banco Ferrouse Agradece a preferência')