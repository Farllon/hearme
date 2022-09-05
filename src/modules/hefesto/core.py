import json
from pathlib import Path

from settings import Settings


class Hefesto:

    def __init__(self) -> None:
        self.__commands = []

    def _create_commands(self, settings: Settings) -> None:
        with open(settings.COMMANDS_FILE_PATH, "r") as f:
            self.__commands = json.load(f)

    def _get_script(self, command: str) -> str:
        for obj in self.__commands:
            if command == str(obj["text"]).upper():
                return Path(obj["script_path"]).read_text()
        
        return ""