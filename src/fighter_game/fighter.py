from random import randint

class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._agility = randint(1,9)
        self._health_points = 100 # Lors de la création d'une instance, les points de vie valent 100.
        
    def get_name(self):
        """Return fighter's name"""
        return self._name
    
    def get_description(self):
        return self._description

    def set_description(self, desc):
        self._description = desc
    
    def get_agility(self):
        return self._agility
    
    def get_strenght(self):
        return 10 - self.get_agility()
    
    def get_health_points(self):
        return self._health_points
    

marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
maurice = Fighter('Maurice', 'The second best one')# on instancie avec les variables de la méthode __init__

print(marcel.get_agility())
print(marcel.get_strenght())



