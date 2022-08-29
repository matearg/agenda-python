class ControlMotor(type): 
    
    def __getitem__(cls, i): 
        return cls.color[i]*5
        
class Auto(metaclass=ControlMotor): 
    color = "Azul"
    def __getitem__(self, indice):            
        return indice ** 0.5
 
print(Auto[1])

objeto = Auto() 
print(objeto[64]) 


"""

class ControlMotor(type): 
    
    def __getitem__(cls, i): 
        return cls.color[i]*5
        
class Auto(metaclass=ControlMotor): 
    color = "Azul"
 
print(Auto[1])
"""