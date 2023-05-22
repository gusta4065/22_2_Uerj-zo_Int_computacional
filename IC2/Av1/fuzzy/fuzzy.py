

class Fuzzy:
    
    def __init__(self,xlimit):
        self.yMax = 1
        self.xMax = xlimit
        self.rules = []

    def addRules(self,name,start, end):
        newRule = {'name':name, 'limits':{'start': start,'end' :end}}
        self.rules.append(newRule)
    def premiseLowerB(self,a,b,x):
        return 1 - (b-x)/(b-a)
    def premiseHigherB(self,c,b,x):
        return 1 - (c-x)/(c-b)



fuzzyTeste = Fuzzy(250)
fuzzyTeste.addRules('Calor_Fraco',50,80)
fuzzyTeste.addRules('Calor_Medio',65,130)
fuzzyTeste.addRules('Calor_Forte',110,180)
fuzzyTeste.addRules('Calor_Critico',165,fuzzyTeste.xMax)
print(fuzzyTeste.rules)


