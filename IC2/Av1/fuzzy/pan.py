"""
          metodos de uma panela
   imaginando uma panela de pressão eletrica, ela pode:
   -abrir *
   -colocar o alimento *
   -fechar *
   -aumentar temperatura
   -diminuir temperatura

    *esse exemplo so tem um alimento então não tara essas funcionalidades

   @@ panela de pressão "pega pressão" com 120° Celsius
   @@ "pega pressão": pressão interna entre 1,44 e 2atm
   @@ 0°C =  273.15K
   @@ Pi/Ti= P/T
   @@ P = Pi*T/Ti
"""

def Celsius_to_kevin(temp):
    return (temp + 273.15)

PRESSAO_I = 1.1 #em atm
TEMP_AMBIANTE = Celsius_to_kevin(25) #25C°   

class Pan:
      
    def __init__(self):
        self.alimento = 'feijão'
        self.tempo = (20*60)
        self.teperature = TEMP_AMBIANTE
        self.pressao = PRESSAO_I
        self.status = 0 # 0 = cru 1 = cozido

    def __final_pressure(self,temp):
        return (PRESSAO_I*temp)/TEMP_AMBIANTE

    def Raise_temp(self):
        self.teperature += 5
        self.pressao = self.__final_pressure(self.teperature)
        print('temp:',self.teperature)
        print('pressão:',self.pressao)

    def Decrease_temp(self):
        self.teperature -= 3
        self.pressao = self.__final_pressure(self.teperature)
        print('pressão:',self.pressao)