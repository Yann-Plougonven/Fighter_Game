class Weapon:
    """
    Class for a weapon
    """
    def __init__(self, name, damage, ammos):
        self._name = name
        self._damage = damage
        self._ammos = ammos
        self._owner = None
    
    def get_name(self):
        """Return fighter's name"""
        return self._name
    
    def get_damage(self):
        return self._damage

    def get_ammos(self):
        return self._ammos
    
    def get_owner(self):
        return self._owner
    
    
    def shoot(self, fighter):
        if self.get_ammos() > 0:
            fighter._health_points -= self.get_damage()
            self._ammos -= 1
            
    def summary(self):
        name = f"name : {self.get_name()}"
        damage = f"damage : {self.get_damage()}"
        ammos = f"ammos : {self.get_ammos()}"
        if self.get_owner():
            owner = f"owner : {self.get_owner().get_name()}"
        else:
            owner = f"owner : "
        return '\n'.join([name, damage, ammos, owner])    



#from fighter_game.fighter import Fighter
#marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
#lance_patates = Weapon("Lance patates", 5, 10)

#lance_patates.shoot(marcel)

#print(marcel.summary())
#print(lance_patates.get_ammos())