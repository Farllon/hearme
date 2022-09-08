from modules.apolo.core import Apolo
from modules.atena.core import Atena
from modules.core.commands import AWAKE, EXIT
from modules.hefesto.core import Hefesto
from settings import Settings
import pyttsx3


class Gaia(Hefesto, Apolo, Atena):

    class States:
        Sleeping = 0
        Awake = 1

    def __init__(self, settings: Settings) -> None:
        super(Hefesto, self).__init__()
        super(Apolo, self).__init__()
        super(Atena, self).__init__()
        self.__settings = settings
        self.__state = self.States.Sleeping
        self.__speak_engine = pyttsx3.init()

    def start(self) -> None:
        self.__speak("Iniciando módulos do sistema GAIA")
        self._create_commands(self.__settings)
        self._create_recognizer(self.__settings)
        self._create_sound_capture()

        self._start_stream()
        self.__speak("Módulos iniciados com sucesso")

        self.__speak("Iniciando processo de conversão de fala")
        self._listen(self.__process)

    def __process(self, data: bytes) -> bool:
        listened_text = self._read_data(data)

        if (listened_text == ""):
            return True

        if listened_text == EXIT:
            self._close()
            return False

        if listened_text == AWAKE:
            self.__state = self.States.Awake
            self.__speak("Ok. Estou te ouvindo.")
            return True

        if self.__state != self.States.Awake:
            return True

        script = self._get_script(listened_text)

        if script != "":
            exec(script)
            self.__state = self.States.Sleeping

        return True
    
    def __speak(self, text: str):
        self.__speak_engine.say(text)
        self.__speak_engine.runAndWait()