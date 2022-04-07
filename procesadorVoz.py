import os
import string

from voice import Voice


class Procesador:
    __slots__ = ['comando', 'parametro', 'texto']

    def __init__(self, a):
        texto = a.getText()
        self.comando = texto[0:texto.find(' ')]
        self.parametro = texto[texto.find(' ') + 1:len(texto)].capitalize()
        self.comandos()
        print(f'{self.comando} {self.parametro}')

    def comandos(self):
        if self.comando == 'abrir' and self.parametro == 'Chrome':
            os.startfile("chrome.exe")
        elif self.comando == 'abrir' and self.parametro == 'Spotify':
            os.startfile('C:/Users/caiol/AppData/Roaming/Spotify/Spotify.exe')
        elif self.comando == 'abrir' and self.parametro == 'Discord':
            os.startfile("C:/Users/caiol/AppData/Local/Discord/app-1.0.9004/Discord.exe")