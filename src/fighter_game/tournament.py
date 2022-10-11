from fighter import Fighter
from myqueue import Queue
fighters_names = ['Michel', 'Jean', 'Gérard', 'Jean-Pierre', 'Chantal', 'Germaine', 'Rachel', 'Odette']


def fight(attaquer, victim):
    """
    En récursif
    Lance un combat entre 2 joueurs
    Retourne le joueur gagnant
    """
    attaquer.punch(victim)
    if victim.get_health_points() <= 0:  # Si la victime est morte
        return attaquer
    else :  # Si la victime est vivante
        return fight(victim, attaquer)
        
def tournament(list_of_fighters):
    """
    Créer un tournoi
    Retourne le survivant du combat
    """
    queue = Queue()
    [queue.enqueue(fighter) for fighter in list_of_fighters]
    while queue.size() > 1:
        queue.enqueue(fight(queue.dequeue(), queue.dequeue()))    
    return queue.dequeue()


fighters = [Fighter(name, "combatant") for name in fighters_names]
print(tournament(fighters).get_name())