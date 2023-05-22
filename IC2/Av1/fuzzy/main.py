import fuzzy
import pan
_fuzzy = fuzzy
_pan = pan


#'iniciando preparo do alimento feijão'


fzT = _fuzzy.Fuzzy(250)
fzT.addRules('Calor_Fraco',50,80)
fzT.addRules('Calor_Medio',65,130)
fzT.addRules('Calor_Forte',110,180)
fzT.addRules('Calor_Critico',165,fzT.xMax)
fzP = _fuzzy.Fuzzy(2.5)
fzP.addRules('Pressao_Fraca',1,1.25)
fzP.addRules('Pressao_Media',1.20,1.45)
fzP.addRules('Pressão_Forte',1.4,1.8)
fzP.addRules('Pressão_Critica',1.75,2.5)

#inciando o cozimento 
panela = _pan.Pan()


"""for tempo in range(panela.tempo):
    if tempo % 15 == 0:  
        panela.Raise_temp()
"""