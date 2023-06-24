import fuzzy
import pan
_fuzzy = fuzzy
_pan = pan

"""
    'iniciando preparo do alimento feijão'
"""
kevin = pan.Celsius_to_kevin
panela = _pan.Pan()
#definindo regras 
fzT = _fuzzy.Fuzzy(250)
fzT.addRules('Calor_Fraco',kevin(0),kevin(80)) 
fzT.addRules('Calor_Medio',kevin(65),kevin(130))
fzT.addRules('Calor_Forte',kevin(110),kevin(180))
fzT.addRules('Calor_Critico',kevin(165),kevin(fzT.xMax))
fzP = _fuzzy.Fuzzy(2.5)
fzP.addRules('Pressao_Fraca',0.5,1.25)
fzP.addRules('Pressao_Media',1.20,1.45)
fzP.addRules('Pressao_Forte',1.4,1.8)
fzP.addRules('Pressao_Critica',1.75,fzP.xMax)


# definindo funçoes
def defuzzicador(mi,regrasA): #mi uma lista de premissas e regrasA lista de regras
    m=[]    
    for regra in regrasA:
        m.append(fzT.getB(fzT.getRuleslimits(regra)['start'],fzT.getRuleslimits(regra)['end']))
    if m.__len__() == 1:# calculo caso somente uma regra
        return (m[0]*mi[0])/(mi[0])
    else:
        return (m[0]*mi[0]+m[1]*mi[1])/(mi[0]+mi[1]) # calculo caso mais de uma regra

def checkRegras(regraT,regraP):
    if regraT == 'Calor_Fraco' and (regraP == 'Pressao_Fraca' or regraP == 'Pressao_Media' or regraP == 'Pressao_Forte'):
        return'Calor_Critico'
    elif regraT == 'Calor_Medio' and (regraP == 'Pressao_Fraca' or regraP == 'Pressao_Media'):
        return'Calor_Critico'
    elif regraT == 'Calor_Medio' and regraP == 'Pressao_Forte':
        return'Calor_Forte'
    elif regraT == 'Calor_Medio' and regraP == 'Pressao_Critica':
        return'Calor_Fraco'
    elif regraT == 'Calor_Forte' and (regraP == 'Pressao_Fraca' or regraP == 'Pressao_Media' or regraP == 'Pressao_Forte'):
        return'Calor_Forte'
    elif regraT == 'Calor_Forte' and regraP == 'Pressao_Critica':
        return'Calor_Fraco'
    elif regraT == 'Calor_Critico' and (regraP == 'Pressao_Fraca' or regraP == 'Pressao_Media'):
        return'Calor_Medio'
    elif regraT == 'Calor_Critico' and regraP == 'Pressao_Critica':
        return'Calor_Fraco'
    else:
        return'Calor_Fraco'
#inciando o cozimento 
"""
    objetivo controlar a temperarura

    se calor baixo e pressão baixa então sobe temperatur
    se calor medio e pressão 
"""

bakingtime = 0
while(panela.status==0): #pan.Celsius_to_kevin(35)
    regraAcionadas= set()
    mi = []
    for regraT in fzT.getRulesNames():
        for regraP in fzP.getRulesNames():
            if fzT.retonarMi(panela.teperature,regraT) > 0 and fzP.retonarMi(panela.pressao,regraP) > 0: #veriffica se alguma regra foi ativada
                regraAcionadas.add(checkRegras(regraT,regraP))
                mi.append(min(fzT.retonarMi(panela.teperature,regraT),fzP.retonarMi(panela.pressao,regraP)))
    print('regras acionadas',list(regraAcionadas))
    newtemp=defuzzicador(sorted(mi,reverse=True),regraAcionadas) #rezultado do calc fuzz
    print('temperatura estimada:',newtemp)
    if panela.teperature < newtemp:
        panela.Raise_temp()
    else:
        panela.Decrease_temp()
    if panela.pressao >= 1.44 and panela.pressao <= 2: #adiciona ao contador depois de pegar pressão
       bakingtime = bakingtime+1
    if(bakingtime==panela.tempo):
        panela.status = 1
print("feijão cozido hora de despresurizar")       
if panela.status==1:
    while(panela.teperature > pan.TEMP_AMBIANTE):
        panela.Decrease_temp()
    print("feijão prontinho")


#while(panela.status==0):
   
    