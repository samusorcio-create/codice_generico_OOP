class Torneo:

    def __init__(self, nome, data, num_partecipanti, quota_iscrizione, premio):
        self.nome = nome
        self.data = data
        self.num_partecipanti = num_partecipanti
        self.quota_iscrizione = quota_iscrizione
        self.premio = premio
        self.partecipanti = []
        self.giochi = []


    def __ep__(self, other):
        if not isinstance(other, Torneo):
            return False
        return self.nome == other.nome and self.data == other.data and self.num_partecipanti == other.num_partecipanti and self.quota_iscrizione == other.quota_iscrizione and self.premio == other.premio
    
    def __repr__(self):
        return f"nome => {self.nome}, data => {self.data}, numnero dei partecipanti => {self.num_partecipanti}, quota di iscrizione => {self.quota_iscrizione}, premio => {self.premio}"

    def postiDisponibili(self):
        return len(self.partecipanti) - self.num_partecipanti

    def isPieno(self):
        if Torneo.postiDisponibili():
            return False
        else:
            return True

    # cliente dovrà essere di tipo Cliente
    def iscriviCliene(self,cliente):
        self.partecipanti.append(cliente)
        
    def visualizzaPartecipanti(self):
        return self.partecipanti
