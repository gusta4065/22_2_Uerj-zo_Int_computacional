"""
          metodos de uma panela
   imaginando uma panela de pressão eletrica, ela pode:
   -abrir
   -colocar o alimento
   -fechar
   -aumentar temperatura
   -diminuir temperatura

   @@ panela de pressão pega pressão com 120° Celsius
   @@ 0°C =  273.15K
   @@ Pi/Ti= P/T
   @@ P = Pi*T/Ti
"""

def Celsius_to_kevin(temp):
    return (temp + 273.15)
def Final_pressure(temp):
    return (PRESSAO_I*temp)/TEMP_AMBIANTE

PRESSAO_I = 1 #em at
TEMP_AMBIANTE = Celsius_to_kevin(25)    

class Pan:
      
    def __init__(self):
        self.alimento = 'feijão'
        self.tempo = (20*60)
        self.teperature = TEMP_AMBIANTE
        self.pressão = PRESSAO_I


    def Raise_temp(self):
        self.teperature += 10
        self.pressão = Final_pressure(self.teperature)

    def Decrease_temp(self):
        self.teperature -= 5
        self.pressão = Final_pressure(self.teperature)
    