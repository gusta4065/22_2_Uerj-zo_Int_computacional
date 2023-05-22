

class Fuzzy:
    
    def __init__(self,xlimit):
        self.yMax = 1
        self.xMax = xlimit
        self.rules = []

    def addRules(self,name,start, end):
        newRule = {'name':name, 'limits':{'start': start,'end' :end}}
        self.rules.append(newRule)
    def getRulesNames(self):
        return [item['name'] for item in self.rules]
    def getRuleslimits(self, name):
        course = self.getRulesNames()
        index = course.index(name)       
        return self.rules[index]['limits']


    def premiseLowerB(self,a,b,x): 
        return 1 - (b-x)/(b-a)
    def premiseHigherB(self,c,b,x):
        return 1 - (c-x)/(c-b)


