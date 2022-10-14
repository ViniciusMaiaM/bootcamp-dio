class cachorro:
    def __init__(self,cor,nome,raca, acordado = True):
        self.cor = cor
        self.nome = nome
        self.raca = raca
        self.acordado = acordado

    def latir(self):
        if self.acordado == True:
            print("AUAUAU")

        else:
            print("O cachorro está dormindo!")

    def dormir(self):
        if self.acordado == True:
            self.acordado = False
            print("ZZZZ....")
        else:
            print("O cachorro já esta dormindo")

cor = input("Qual a cor do seu cachorro? ")
nome = input("Qual o nome do seu cachorro? ")
raca = input("Qual a raca do seu cachorro? ")

c1 = cachorro(cor,nome,raca, False)


c1.latir()

c1.dormir()

print(c1.acordado)