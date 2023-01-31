especialista = [[0,1], 
                [1,0],
                ]

vectAwnser = [0]
soma = 0

i=0
while i<2:
    if(especialista[0][i]== vectAwnser[0]):
        vectAwnser.append(1)
    i= i + 1

i = 0
while i<2 :
    if((especialista[0][i]== vectAwnser[0]) and (especialista[1][i] == vectAwnser[1]) ):
        soma = especialista[0][i] + especialista[1][i]
    i = i + 1

if(soma <1):
    print('bolsa está em alta')
else:
    print('bolsa está em baixa')


