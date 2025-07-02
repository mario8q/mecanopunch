# Class player and enemy (system)
from .game import GameObject

class Player(GameObject):
    """
    Clase para el jugador principal del juego
    """
    def __init__(self, player_name: str, x: int, y: int) -> None:
        super().__init__(x, y, 50, 50, color="yellow")
        self.player_name = player_name
        self.lives: int = 8
        self.score: int = 0
    
    def take_damage(self) -> bool:
        """
        Funcion para restar la vida del jugador principal
        """
        if self.lives > 0:
            self.lives -= 1
            return True
        return False
    
    def heal(self) -> None:
        """
        Funcion para sumar la vida del jugador principal
        """
        self.lives += 1

    def add_score(self, points) -> None:
        """
        Funcion para sumar puntos al score del jugador principal
        """
        self.score += points

class Enemy(GameObject):
    """
    Clase para el enemigo del jugador principal (sistema)
    """
    def __init__(self, enemy_name: str, x: int, y: int) -> None:
        super().__init__(x, y, 50, 50, color="purple")
        self.enemy_name = enemy_name

    

        
