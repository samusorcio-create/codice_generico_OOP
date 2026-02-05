class Gioco:

    def __init__(self, titolo, editore_nome, editore_nazione,
                prezzo,min_giocatori,max_giocatori,durata_media,tipo,quantita):
        self.titolo = titolo
        self.editore_nome = editore_nome
        self.editore_nazione = editore_nazione
        self.prezzo = prezzo
        self.min_giocatori = min_giocatori
        self.max_giocatori = max_giocatori
        self.durata_media = durata_media
        self.tipo = tipo
        self.quantita = quantita

def __eq__(self, other):
    if not isinstance(other,Gioco):
        return False
    # da completare
    return self.titolo == other.titolo 

def __repr__(self):
    # da completare
    return f"titolo => {self.titolo} " 

def isDisponibile(self):
    return self.quantita > 0
