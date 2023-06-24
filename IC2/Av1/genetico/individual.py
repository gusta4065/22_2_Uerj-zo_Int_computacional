import random


GENES ='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET= "TIQUINHO SOARES E FODA!!!"


class Individual:

    def __init__(self,chrom):
        self.chromosome = chrom
        self.fit = self.get_fit()


    #calculando o grau de compatibilidade
    def get_fit(self):
        #print(self.chromosome)
        fit = 0
        for chars, chart in zip(self.chromosome,TARGET):
            if chars != chart: fit+= 1
        return fit

    def __mutation(self):
        return random.choice(GENES)
    def create_genome(self):
        return[self.__mutation(self) for _ in range(len(TARGET))]
    def mating(self,part):
        child = []
        for chars, charp in zip(self.chromosome, part.chromosome):
            prob = random.random()

            if prob < 0.45:
                child.append(chars)
            elif prob < 0.90:
                child.append(charp)
            else:
                child.append(self.__mutation())
        return Individual(child)
