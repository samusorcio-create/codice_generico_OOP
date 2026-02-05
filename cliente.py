class Cliente:

    def __init__(self, nome, num_tessera, punti_fedelta):
        self.nome = nome
        self.num_tessera = num_tessera
        self.punti_fedelta = punti_fedelta

    def __repr__(self):
        return f"nome => {self.nome}, numero di tessera => {self.num_tessera}, punti fedelta => {self.punti_fedelta}"

# promemoria usare il singolare per le noominazioni delle classi 

    def __eq_(self, other):
        if not isinstance(other, Cliente):
            return False
        return self.nome == other.nome and self.num_tessera == other.num_tessera and self.punti_fedelta == other.punti_fedelta 