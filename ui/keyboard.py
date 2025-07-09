import tkinter as tk
from random import choice, choices
import tkinter.font as tkf
from typing import Dict, List, Optional, Union

import keyboardlayout as kl
import keyboardlayout.tkinter as klt
from keyboardlayout.layouts import LayoutName
from keyboardlayout.key import Key

class VirtualKeyboard:
    """
    Clase para crear el teclado virtual base del juego
    """
    def __init__(self, master: tk.Tk, key_size: int = 95) -> None:
        self.master = master
        self.key_size = key_size
        self.layout_name: LayoutName = LayoutName.QWERTY # type: ignore[attr-defined]
        self.create_keyboard()

    def create_keyboard(self):
        # Colores y estilos
        blasphemy_color: str = "#581223"
        self.keyboard_info: kl.KeyboardInfo = kl.KeyboardInfo(
            position=(0, 0),
            padding=4,
            color=blasphemy_color
        )
        # Configs del teclado
        self.key_info: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#745874", # Color de fondo 745874, 72505A
            txt_color='#222222', # Texto oscuro
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10) # Reduce el espacio, se verá más centrado
        )

        # Creamos un nuevo estilo visual para resaltar
        self.pressed_style: kl.KeyInfo = kl.KeyInfo(
            margin=10,
            color="#702038", # Fondo 
            txt_color="#b3b2b2", # Letra blanca
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(0, 5)
        )

        self.released_style: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#745874", 
            txt_color='#222222', 
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'), 
            txt_padding=(5, 10)
        )

        self.active_keys: set[str] = set()

        self.letter_key_size: tuple = (self.key_size, self.key_size)

        # Crear teclado virtual y almacenarlo como atributo
        self.keyboard: klt.KeyboardLayout = klt.KeyboardLayout(
            self.layout_name,
            self.keyboard_info,
            self.letter_key_size,
            self.key_info,
            master=self.master
        )
        self.bind_keyboard_events()
    
    def get_widget(self) -> tk.Frame:
        """
        Devuelve el widget de teclado 'base' para usar en otras pantallas
        """
        return self.keyboard
    
    def bind_keyboard_events(self) -> None:
        """
        Asociar eventos de teclado al teclado virtual
        """
        self.master.bind("<Key>", self.on_key_press)
        self.master.bind("<KeyRelease>", self.on_key_release)
    
    def on_key_press(self, event) -> None:
        """
        Callback func para key press events 
        """
        keysym: str = event.keysym
        self.active_keys.add(keysym)

        key: Optional[kl.Key] = self.keyboard.get_key(event)

        if key:
            self.keyboard.update_key(key, self.pressed_style)
            print(f"Key press: {event.keysym}")

    def on_key_release(self, event) -> None:
        """
        Callback func para key release events
        """
        keysym: str = event.keysym
        if keysym not in self.active_keys and "Shift" in keysym:
            if "Shift_L" in self.active_keys:
                keysym = "Shift_L"
            elif "Shift_R" in self.active_keys:
                keysym = "Shift_R"

        self.active_keys.discard(keysym)

        if keysym == "Shift_R":
            key: Optional[kl.Key] = kl.Key.RIGHT_SHIFT
        elif keysym == "Shift_L":
            key: Optional[kl.Key] = kl.Key.LEFT_SHIFT
        else:
            key: Optional[kl.Key] = self.keyboard.get_key(event)

        if key:
            self.keyboard.update_key(key, self.released_style)
        print(f"Key released: {event.keysym}") 

    def unbind_keyboard_events(self) -> None:
        """
        Funcion para desvincular eventos del teclado
        """
        self.master.unbind("<Key>")
        self.master.unbind("<KeyRelease>")

class VirtualKeyboardCorrupted(VirtualKeyboard):
    """
    Clase para crear el teclado virtual 'corrupto' del juego
    """
    CORRUPTED_KEYS: Dict[str, str] = {
        'q': 'p',
        'p': 'q',
        'w': 'o',
        'o': 'w',
        'e': 'i',
        'i': 'e',
        'r': 'u',
        'u': 'r',
        't': 'y',
        'y': 't',
        'Q': 'P',
        'P': 'Q',
        'W': 'O',
        'O': 'W',
        'E': 'I',
        'I': 'E',
        'R': 'U',
        'U': 'R',
        'T': 'Y',
        'Y': 'T',
        'a': 'l',
        'l': 'a',
        's': 'k',
        'k': 's',
        'd': 'j',
        'j': 'd',
        'f': 'h',
        'h': 'f',
        'g': 'v',
        'v': 'g',
        'A': 'L',
        'L': 'A',
        'S': 'K',
        'K': 'S',
        'D': 'J',
        'J': 'D',
        'F': 'H',
        'H': 'F',
        'G': 'V',
        'V': 'G',
        'z': 'm',
        'm': 'z',
        'x': 'n',
        'n': 'x',
        'c': 'b',
        'b': 'c',
        'Z': 'M',
        'M': 'Z',
        'X': "N",
        'N': "X",
        'C': 'B',
        'B': 'C',
    }
    def create_keyboard(self):
        """
        Override para crear el teclado 'corrupto' del juego
        """
        self.layout_name: LayoutName = LayoutName.QWERTY  # type: ignore[attr-defined]
        corrupted_color: str = "#350808"
        self.keyboard_info: kl.KeyboardInfo = kl.KeyboardInfo(
            position=(0, 0),
            padding=4,
            color=corrupted_color
        )
        self.key_info: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#25194e",
            txt_color="#b3b2b2",
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10)
        )

        self.released_style: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#25194e",
            txt_color="#b3b2b2",
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10)
        )

        self.active_keys: set[str] = set()

        self.letter_key_size: tuple = (self.key_size, self.key_size)

        self.keyboard: klt.KeyboardLayout = klt.KeyboardLayout(
            self.layout_name,
            self.keyboard_info,
            self.letter_key_size,
            self.key_info,
            master=self.master
        )
        self.bind_keyboard_events()

        self.special_corrupted_keys: Dict[kl.Key, str] = { 
            Key.Q: "#a000b4",
            Key.W: "#a000b4",
            Key.E: "#a000b4",
            Key.R: "#a000b4",
            Key.T: "#a000b4",
            Key.Y: "#a000b4",
            Key.U: "#a000b4",
            Key.I: "#a000b4",
            Key.O: "#a000b4",
            Key.P: "#a000b4",

            Key.A: "#7a0089",      
            Key.S: "#7a0089",      
            Key.D: "#7a0089",              
            Key.F: "#7a0089",
            Key.G: "#7a0089",
            Key.H: "#7a0089",               
            Key.J: "#7a0089",               
            Key.K: "#7a0089",               
            Key.L: "#7a0089",               

            Key.Z: "#550056",
            Key.X: "#550056",
            Key.C: "#550056",
            Key.V: "#550056",
            Key.B: "#550056",
            Key.N: "#550056",
            Key.M: "#550056",
        }

        for key, color in self.special_corrupted_keys.items():
            self.custom_keys_style: kl.KeyInfo = kl.KeyInfo(
                margin=4,
                color=color,
                txt_color="#b3b2b2",
                txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
                txt_padding=(5, 10)
            )

            self.keyboard.update_key(key, self.custom_keys_style)

    def translate_corrupted_keys(self, symbol: str) -> str:
        """
        Funcion que traduce los simbolos del teclado cambiando su orden
        """
        return self.CORRUPTED_KEYS.get(symbol, symbol)

    def on_key_press(self, event) -> None:
        """
        Override para pressed keys
        """
        keysym: str = event.keysym
        self.active_keys.add(keysym)
        
        corrupted_keys_colors: List[str] = ["#40ff40", "#e12e7a", "#c900ff", "#f9fb00"]
        random_corrupted_color: str = choice(corrupted_keys_colors)
        pressed_style: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color=random_corrupted_color,
            txt_color="#eeeeee",
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10)
        )

        translated: str = self.translate_corrupted_keys(keysym)
        matching_key: Union[Optional[kl.Key], None] = next((k for k in Key if k.value == translated), None)
            
        key: Optional[kl.Key] = self.keyboard.get_key(event)

        if matching_key:   
            self.keyboard.update_key(matching_key, pressed_style)
        elif key:
            self.keyboard.update_key(key, pressed_style)

        print(f"Key pressed: {event.keysym}")
        print(f"Original: {matching_key} → Corrupto: {translated}")
        # Usar translated para la logica del teclado corrupto

    def on_key_release(self, event) -> None:
        """
        Override para released events en key
        """
        keysym: str = event.keysym
        if keysym not in self.active_keys and "Shift" in keysym:
            if "Shift_L" in self.active_keys:
                keysym = "Shift_L"
            elif "Shift_R" in self.active_keys:
                keysym = "Shift_R"

        self.active_keys.discard(keysym)

        translated: str = self.translate_corrupted_keys(event.keysym)
        matching_key: Union[Optional[kl.Key], None] = next((k for k in Key if k.value == translated), None)

        if keysym == "Shift_R":
            key: Optional[kl.Key] = kl.Key.RIGHT_SHIFT
        elif keysym == "Shift_L":
            key: Optional[kl.Key] = kl.Key.LEFT_SHIFT
        else:
            key = self.keyboard.get_key(event)

        if matching_key:
            self.keyboard.update_key(matching_key, self.released_style)
        elif key:
            self.keyboard.update_key(key, self.released_style)

        for key, color in self.special_corrupted_keys.items():
            self.custom_keys_style: kl.KeyInfo = kl.KeyInfo(
                margin=4,
                color=color,
                txt_color="#b3b2b2",
                txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
                txt_padding=(5, 10)
            )
            self.keyboard.update_key(key, self.custom_keys_style)
        
        print(f"Key released: {event.keysym}")
        print(f"Original: {matching_key} → Corrupto: {translated}")

class VirtualKeyboardCorruptedBackSpace(VirtualKeyboardCorrupted):
    """
    Clase para crear una variacion de teclado con la tecla backspace corrupta
    """
    def create_keyboard(self):
        """
        Override para crear el teclado corrupto con la tecla backspace unica
        """
        self.layout_name: LayoutName = LayoutName.QWERTY  # type: ignore[attr-defined]
        corrupted_color: str = "#350808"
        self.keyboard_info: kl.KeyboardInfo = kl.KeyboardInfo(
            position=(0, 0),
            padding=4,
            color=corrupted_color
        )
        self.key_info: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#25194e",
            txt_color="#b3b2b2",
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10)
        )

        self.released_style: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#25194e",
            txt_color="#b3b2b2",
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10)
        )

        self.active_keys: set[str] = set()

        self.letter_key_size: tuple = (self.key_size, self.key_size)

        self.keyboard: klt.KeyboardLayout = klt.KeyboardLayout(
            self.layout_name,
            self.keyboard_info,
            self.letter_key_size,
            self.key_info,
            master=self.master
        )
        self.bind_keyboard_events()
        
        self.custom_keys_style: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#a000b4",
            txt_color="#b3b2b2",
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10)
        )

        self.keyboard.update_key(kl.Key.BACKSPACE, self.custom_keys_style)

    def translate_corrupted_keys(self, symbol: str) -> str:
        if symbol == "BackSpace":
            return "None"  # Mapeamos a una tecla inexistente para que no reaccione
        return symbol
    
    def on_key_release(self, event) -> None:
        """
        Override para released events en key para actualizar la tecla backspace
        """
        keysym: str = event.keysym
        if keysym not in self.active_keys and "Shift" in keysym:
            if "Shift_L" in self.active_keys:
                keysym = "Shift_L"
            elif "Shift_R" in self.active_keys:
                keysym = "Shift_R"

        self.active_keys.discard(keysym)

        translated: str = self.translate_corrupted_keys(event.keysym)
        matching_key: Union[Optional[kl.Key], None] = next((k for k in Key if k.value == translated), None)

        if keysym == "Shift_R":
            key: Optional[kl.Key] = kl.Key.RIGHT_SHIFT
        elif keysym == "Shift_L":
            key: Optional[kl.Key] = kl.Key.LEFT_SHIFT
        else:
            key = self.keyboard.get_key(event)

        if matching_key:
            self.keyboard.update_key(matching_key, self.released_style)
        elif key:
            self.keyboard.update_key(key, self.released_style)

        self.custom_keys_style: kl.KeyInfo = kl.KeyInfo(
            margin=4,
            color="#a000b4",
            txt_color="#b3b2b2",
            txt_font=tkf.Font(family='Terminal', size=18, weight='bold'),
            txt_padding=(5, 10)
        )
        self.keyboard.update_key(kl.Key.BACKSPACE, self.custom_keys_style)
        
        print(f"Key released: {event.keysym}")
        print(f"Original: {matching_key} → Corrupto: {translated}")
    
