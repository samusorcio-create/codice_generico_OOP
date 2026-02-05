class Aquisto:

        def __init__(self, prezzo, reteizzato, data):
                self.prezzo = prezzo
                self.reteizzato = reteizzato
                self.data = data    
                self.gioco = []

        def __repr__(self):
            return f"pezzo =>{self.prezzo}, reteizzato =>{self.reteizzato}, data =>{self.data}"
            
        def __eq__(self, other):
            if not isinstance(other, Aquisto):
                return False    
            return self.prezzo == other.prezzo and self.reteizzato == other.reteizzato and self.data == other.data
         