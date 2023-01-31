especialista = [[0,1], 
                [1,0],
                ]

vectAwnser = []
JAnwswer = -1
soma = 0

# A bolsa está em baixa ?
# ra isso precisa sabar a taxa de juros 2
# e pra saber o juros precisa do dolar 1

print('O dolar esta em alta ou em baixa')
print('1 para sim e 0 para não')




dolar = 0
i = 0

if(dolar == 0):
    vectAwnser.append(0)
    JAnwswer = 1
else:
    vectAwnser.append(1)
    JAnwswer = 0

if(JAnwswer):
    vectAwnser.append(1)

while i<2 :
    if((especialista[0][i]== vectAwnser[0]) and (especialista[1][i] == vectAwnser[1]) ):
        soma = especialista[0][i] + especialista[1][i]
    i = i + 1

if(soma <1):
    print('bolsa está em alta')
else:
    print('bolsa está em baixa')
