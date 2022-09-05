from modules.core.gaia import Gaia
from settings import Settings


def main() -> None:
    settings = Settings()

    gaia = Gaia(settings)
    gaia.start()

if __name__ == "__main__":
    main()