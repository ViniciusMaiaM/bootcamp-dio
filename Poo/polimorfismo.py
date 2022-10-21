class Passaro:
    def voar(self):
        print("Voando!")

class Arara(Passaro):
    def voar(self):
        super().voar()

class Pinguim(Passaro):
    def voar(self):
        print("Pinguim não consegue voar")

class Avião(Passaro):
    def voar(self):
        print("O avião está voando")
    
def plano_voo(teste):
    teste.voar()

plano_voo(Arara())
plano_voo(Avião())
plano_voo(Pinguim())