from abc import ABC, abstractmethod, abstractproperty


class Controle_remoto:
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass
    # Também é possibel definir propriedades abstratas para a classe

class Controle_tv(Controle_remoto):
    def ligar(self):
        print("Ligando TV")

    def desligar(self):
        print("Desligando a TV")

    def marca(self):
        return "LG"

class Controle_ar_condicionado(Controle_remoto):
    def ligar(self):
        print("Ligando o ar condicionado")
    
    def desligar(self):
        print("Desligando o ar condicionado")

    def marca(self):
        return "Consul"

controle = Controle_tv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = Controle_ar_condicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

# Quando se faz o contrato e se herda a classe pai, é necessário implementar todos os métodos abstratos
# dessa classe pai na filha