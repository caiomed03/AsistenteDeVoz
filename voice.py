import speech_recognition as sr



class Voice:
    __slots__ = ["r", "text"]

    def getText(self):
        return self.text

    def __init__(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak Anything : ')
            audio = self.r.listen(source)

            try:
                self.text = self.r.recognize_google(audio, language="es-ES")
            except:
                print('Sorry could not hear')


