class Voiture():
    litres = 100
    def essence(self):
        print(self.litres)

    def afficher_reservoir(self):
        print(f"La voiture contient {self.litres} litres d’essence")

    def roule(self, km):
        self.litres = self.litres - ((km*5)/100)
        if self.litres > 10:
            print(f"La voiture contient {self.litres} litres d’essence")
        elif self.litres <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            self.litres = 0.0
            print(f"La voiture contient {self.litres} litres d’essence")
        else:
            print("Vous n'avez bientôt plus d'essence !")
            print(f"La voiture contient {self.litres} litres d’essence")

    def faire_le_plein(self):
        self.litres = 100
        print("Vous pouvez repartir !")
