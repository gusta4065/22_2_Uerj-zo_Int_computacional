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
fzP.addRules('Pressão_Forte',1.4,1.8)
fzP.addRules('Pressão_Critica',1.75,fzP.xMax)


# definindo funçoes
def defuzzicador(miT,miP,regrasA):
    return

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

#inciando o cozimento 
"""
    objetivo controlar a temperarura

    se calor baixo e pressão baixa então sobe temperatur
    se calor medio e pressão 
"""


while(panela.teperature <= kevin(70)): #pan.Celsius_to_kevin(35)
    panela.Raise_temp()
    regraAcionadas= set()
    for regraT in fzT.getRulesNames():
        for regraP in fzP.getRulesNames():
            regraAcionadas.add(checkRegras(regraT,regraP))
    print('regraT:',regraT,'RegraP:',regraP)
    print('dois valores mais altos')




#while(panela.status==0):
   
    