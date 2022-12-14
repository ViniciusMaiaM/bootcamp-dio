class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, ** kw):
        self.cor_pelo = cor_pelo
        super().__init__(num_patas=kw["num_patas"])
        # super é utilizado para chamar o construtor pai

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        # As duas maneiras são validas para a utilização de kw


class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return ("Oi, estou falando!")
    # Classe criada para que se faça apenas aquilo e seja reutilizada
    # em diferentes classes

class Ornitorrico(Mamifero,Animal, FalarMixin):
    def __init__(self,cor_pelo,cor_bico,num_patas):
        # print(Ornitorrico.__mro__)
        # Assim conseguimos a ordem de resolução/leitura 
        # dos atributos e metodos

        super().__init__(cor_pelo=cor_pelo,
        cor_bico=cor_bico,num_patas=num_patas)
        # Definindo novamente os construtores

gat = Gato(num_patas=4, cor_pelo="Branco")
print(gat)
# Utilizando o kw é necessário utilizar essa declaração 
# quando se utiliza a classe



orn = Ornitorrico(num_patas=4,cor_pelo="Marrom",cor_bico="Amarelo")
print(orn.falar())

# Para evitar problemas se retira os argumentos 
# que são da classe filha e também na classe pai
# e se utiliza o kw 