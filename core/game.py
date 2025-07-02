
class GameObject:
    """
    Clase base para objetos del juego
    """
    def __init__(self, x, y, width, height, color="blue"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.active = True
    
    def update(self):
        """
        Método para actualizar el objeto (override en subclases)
        """
        pass
    
    def draw(self, canvas):
        """
        Método para dibujar el objeto (override en subclases)
        """
        pass