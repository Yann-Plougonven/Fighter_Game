from random import randint, uniform

class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._agility = randint(1,9)
        self._health_points = 100 # Lors de la création d'une instance, les points de vie valent 100.
        self._weapon = None
        
    def get_name(self):
        """Return fighter's name"""
        return self._name
    
    def get_description(self):
        return self._description

    def set_description(self, desc):
        self._description = desc
    
    def get_agility(self):
        return self._agility
    
    def get_strength(self):
        return 10 - self.get_agility()
    
    def get_health_points(self):
        return self._health_points
    
    def get_weapon(self):
        return self._weapon
    
    def take_weapon(self, a_weapon): # à son initiative, le fighter prend ou change d'arme
        if self.get_weapon(): # Si self a déjà une arme, on enlève sa pocession à son ex owner
            old_weapon = self.get_weapon()
            old_weapon._owner = None
        # Dans tous les cas, on associe la nouvelle arme à son owner :
        self._weapon = a_weapon
        a_weapon._owner = self
            
    
    def punch(self, aFighter):
        """
        punch aFighter
        return the health points of AFighter
        """
        points=int(uniform(0.7,1.0)*10*self.get_strength()/aFighter.get_agility())
        aFighter._health_points=aFighter.get_health_points()-points
        #print(aFighter._health_points)
        return aFighter.get_health_points()
    
    def shoot(self, aFighter):
        if self.get_weapon():
            self.get_weapon().shoot(aFighter)
        else :
            self.punch(aFighter)
        
    
    def summary(self):
        name = f"name : {self.get_name()}"
        description = f"description : {self.get_description()}"
        agility = f"agility : {self.get_agility()}"
        strength = f"strength : {self.get_strength()}"
        health_points = f"health points : {self.get_health_points()}"
        if self.get_weapon():
            weapon = f"weapon : {self.get_weapon().get_name()}"
        else:
            weapon = f"weapon : "
        return "\n".join([name, description, agility, strength, health_points, weapon])
        
    
# from weapon import Weapon
# 
# lance_patates = Weapon("Lance patates", 5, 10)
# bazooka = Weapon("Bazooka", 20, 2)
# print(bazooka.summary())
# marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
# maurice = Fighter('Maurice', 'The second best one')# on instancie avec les variables de la méthode __init__
# 
# marcel.take_weapon(lance_patates)
# print(maurice.summary())
# marcel.shoot(maurice)
# print(maurice.summary())
# marcel.take_weapon(bazooka)
# print(bazooka.summary())
# marcel.shoot(maurice)
# print(maurice.summary())
# print(lance_patates.get_owner())
# print(bazooka.get_owner())
# print(f"\n {marcel.summary()}")

# 
# while marcel.get_health_points() > 0 and maurice.get_health_points() > 0:
#     marcel.punch(maurice)
#     if maurice.get_health_points() > 0:
#         maurice.punch(marcel)
# 
# if marcel.get_health_points() > 0:
#     print(f"Le gagnant est {marcel.get_name()}")
# else :
#     print(f"Le gagnant est {maurice.get_name()}")
# 
# 
# print(marcel.summary())
# print(maurice.summary())
# #print(marcel.get_agility())
# #print(marcel.get_strenght())