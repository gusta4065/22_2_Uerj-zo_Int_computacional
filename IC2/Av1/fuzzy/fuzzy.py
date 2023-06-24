class Fuzzy:
    
    def __init__(self,xlimit):
        self.yMax = 1
        self.xMax = xlimit
        self.rules = []


    #definindo regras
    def addRules(self,name,start, end):
        newRule = {'name':name, 'limits':{'start': start,'end' :end}}
        self.rules.append(newRule)
    def getRulesNames(self):
        return [item['name'] for item in self.rules]
    def getRuleName(self, name):
        course = self.getRulesNames()
        index = course.index(name)       
        return self.rules[index]
    def getRuleslimits(self, name):
        course = self.getRulesNames()
        index = course.index(name)       
        return self.rules[index]['limits']
    

    #calclando premissas
    def getB(self,a,c):
        return (a+c)/2
    def __premiseLowerB(self,a,b,x):
        return 1 - (b-x)/(b-a)
    def __premiseHigherB(self,b,c,x):
        return 1 - (c-x)/(c-b)
    def __getPremise(self,a,c,x):
        b = self.getB(a,c)
        if x<=b:
            return self.__premiseLowerB(a,b,x)
        else:
            return self.__premiseHigherB(b,c,x)
        
    """def retornaUPremissa(self,x):
        premissaV = []
        for regra in self.getRulesNames():
            start = self.getRuleslimits(regra)['start']
            end = self.getRuleslimits(regra)['end']
            if x >= start and x <= end:
                premissaV.append(self.__getPremise(start,end,x))
        return premissaV"""
    

    def retonarMi(self,x,name):
        start = self.getRuleslimits(name)['start']
        end = self.getRuleslimits(name)['end']
        if x >= start and x <= end:
            return self.__getPremise(start,end,x)
        else:
            return 0.0