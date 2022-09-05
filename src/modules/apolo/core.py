import pyaudio

class Apolo:

    def __init__(self) -> None:
        self.__capture: pyaudio.PyAudio = None
        self.__stream: pyaudio.Stream = None
        
    def _create_sound_capture(self) -> None:
        self.__capture = pyaudio.PyAudio()

    def _start_stream(self) -> None:
        self.__stream = self.__capture.open(
            format=pyaudio.paInt16,
            rate=16000, 
            input=True,
            input_device_index=1,
            frames_per_buffer=8192)

        self.__stream.start_stream()

    def _close(self) -> None:
        self.__stream.stop_stream()
        self.__stream.close()
        
        self.__capture.terminate()

    def _listen(self, func) -> None:
        execute_again = True

        try:
            while execute_again:
                data = self.__stream.read(4096, exception_on_overflow=False)
                execute_again = func(data)
        except KeyboardInterrupt:
            self._close()