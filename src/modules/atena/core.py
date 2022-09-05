import json
from vosk import Model, KaldiRecognizer

from settings import Settings


class Atena:

    def __init__(self) -> None:
        self.__recognizer: KaldiRecognizer = None

    def _create_recognizer(self, settings: Settings) -> None:
        model = Model(lang = "pt-br", model_path = settings.VOSK_FOLDER_PATH)
        self.__recognizer = KaldiRecognizer(model, 16000)

    def _read_data(self, data: bytes) -> str:
        if self.__recognizer.AcceptWaveform(data):
            return str(json.loads(self.__recognizer.Result())["text"]).upper()
        else:
            return ""