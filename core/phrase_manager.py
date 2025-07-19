from typing import Dict, List, Set
from game_object import GameObject
from random import choice
class PhraseManager:
    """
    Clase para cargar las frases de los archivos txt segun la dificultad
    """
    def __init__(self, base_path: str) -> None:
        self.paths: Dict[str, str] = {
            "EASY" : f"{base_path}\\easy_phrases.txt",
            "MEDIUM" : f"{base_path}\\medium_phrases.txt",
            "HARD" : f"{base_path}\\hard_phrases.txt"
        }
        self.phrases: Dict[str, List[str]] = {level : self.load_phrase(path) for level, path in self.paths.items()}
        self.used_phrases: Dict[str, Set[str]] = {level: set() for level in self.paths}

    def load_phrase(self, path: str) -> List[str]:
        """
        Metodo para cargar las frases de los archivos en una lista 
        """
        with open(path, "r", encoding="UTF-8") as file:
            self.list_phrases: List[str] = [
                line.strip() 
                for line in file
                if line.strip() and not line.strip().startswith("#")
                ]
            return self.list_phrases
        
    def get_random_phrase(self, difficulty: str) -> str:
        """
        Metodo para obtener una frase random no duplicada segun la dificultad
        """
        level: str = difficulty.upper()
        all_phrases: List[str] = self.phrases.get(level, [""])
        used: Set[str] = self.used_phrases.get(level, set())

        if not all_phrases:
            return "No phrase was found"
        
        if len(used) >= len(all_phrases):
            used.clear()
        
        avaliable_phrases: List[str] = [phrase for phrase in all_phrases if not phrase in used]
        
        self.random_phrase: str = choice(avaliable_phrases)
        used.add(self.random_phrase)

        return self.random_phrase
        
class TypingPhrase(GameObject):
    def __init__(self, phrase: str, x: int, y: int, width: int, height: int, color: str = "black") -> None:
        super().__init__(x, y, width, height, color)

phrase_manager = PhraseManager("data")

print(phrase_manager.get_random_phrase("EASY"))
print(phrase_manager.get_random_phrase("medium"))
print(phrase_manager.get_random_phrase("Hard"))



