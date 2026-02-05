# gestionale per la ludoteca tana del cilling
# classe main di test
# v1.0
# authors: 1 SW 2025
from gioco import Gioco

if __name__ == "__main__":
    print("ludoteca tana del cinùling")

    #fase di test 

    g_dixit = Gioco("Dixit", "asmodee", "francese", 24.3, 3, 4, 2, "tavolo", 1)

    print(g_dixit)
    print(g_dixit.isDisponibile())
