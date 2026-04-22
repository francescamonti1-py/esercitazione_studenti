class Studente:
    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []

    def presentati(self):
        return f"Salve sono {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}"

    def aggiungi_voto(self, voto):
        if 18 <= voto <= 30:
            self.voti.append(voto)
            print(f"Voto {voto} registrato correttamente per {self.nome}.")
        elif voto < 18:
            print(f"Esame non superato: il voto {voto} è insufficiente.")
        else:
            print("Errore: un voto non può essere superiore a 30.")

    def calcola_media(self):
        if not self.voti:
            return 0
        media = sum(self.voti) / len(self.voti)
        return round(media, 2)

    def studia(self, ore):
        print(f"{self.nome} ha studiato per {ore} ore.")


studente1 = Studente("Mario", "Rossi", 30, "A165")
studente2 = Studente("Carla", "Verdi", 21, "B490")

print(studente1.presentati())
studente1.aggiungi_voto(27)
studente1.aggiungi_voto(25)
studente1.studia(4)
print(f"Media di {studente1.nome}: {studente1.calcola_media()}")

print("-" * 30)

print(studente2.presentati())
studente2.aggiungi_voto(23)
studente2.studia(2)
print(f"Media di {studente2.nome}: {studente2.calcola_media()}")
