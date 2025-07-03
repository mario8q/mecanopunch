import tkinter as tk
import tkinter.font as tkf
from typing import Optional

import keyboardlayout as kl
import keyboardlayout.tkinter as klt
from keyboardlayout.layouts import LayoutName

class VirtualKeyboard:
    """
    Clase para crear el teclado virtual del juego
    """
    def __init__(self, master: tk.Tk, key_size: int = 60) -> None:
        self.master = master
        # Estilo del teclado
        self.layout_name: LayoutName = LayoutName.QWERTY # type: ignore[attr-defined]

        dark_grey: str = "#F16D20"

        # Configs del teclado
        self.keyboard_info: kl.KeyboardInfo = kl.KeyboardInfo(
            position=(0, 0),
            padding=2,
            color=dark_grey
        )

        self.key_info: kl.KeyInfo = kl.KeyInfo(
            margin=3,
            color='#dddddd',           # Color de fondo claro
            txt_color='#222222',       # Texto oscuro
            txt_font=tkf.Font(family='Courier New', size=16, weight='bold'),  # Estilo máquina de escribir
            txt_padding=(10, 10)       # Reduce el espacio, se verá más centrado
        )

        self.letter_key_size: tuple = (key_size, key_size)

        # Crear teclado virtual y almacenarlo como atributo
        self.keyboard = klt.KeyboardLayout(
            self.layout_name,
            self.keyboard_info,
            self.letter_key_size,
            self.key_info,
            master=master
        )

        self.bind_keyboard_events()
    
    def get_widget(self) -> tk.Frame:
        """
        Devuelve el widget de teclado para usar en otras pantallas
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
        key: Optional[kl.Key]  = self.keyboard.get_key(event)
        if key:
            # Creamos un nuevo estilo visual para resaltar
            pressed_style: kl.KeyInfo = kl.KeyInfo(
                margin=10,
                color="#770808",           # Fondo rojo
                txt_color="#ffffff",       # Letra blanca
                txt_font=tkf.Font(family='Arial', size=16, weight='bold'),
                txt_padding=(10, 10)
            )
            self.keyboard.update_key(key, pressed_style)
            print(f"Key released: {event.keysym}")

    def on_key_release(self, event) -> None:
        """
        Callback func para key release events
        """
        key: Optional[kl.Key] = self.keyboard.get_key(event)
        if key:
            released_style: kl.KeyInfo = kl.KeyInfo(
                margin=3,
                color='#dddddd',           
                txt_color='#222222',       
                txt_font=tkf.Font(family='Courier New', size=16, weight='bold'),  
                txt_padding=(10, 10) 
            )
            self.keyboard.update_key(key, released_style)
        print(f"Key released: {event.keysym}")  
    
