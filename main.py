from pynput import keyboard

from procesadorVoz import Procesador
from voice import Voice


class Main:
    def __init__(self):
        a = Voice()
        Procesador(a)

def on_press(key):
    if key == keyboard.Key.esc:
        return False
    try:
        k = key.char
    except:
        k = key.name
    if k in ['ñ']:
        Main()

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
