class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =  idade

    @classmethod
    def criar_data_nasc(cls,ano,mes,dia,nome):
        idade = 2022 - ano
        return cls(nome,idade)

    # Se utiliza o decorador "classmethod" para um método de classe
    # Com métodos de classe a convenção é utilizar cls no lugar de self
    # cls é uma instância da classe

    @staticmethod
    def maior_idade(idade):
        return idade >= 18

    # Decorador "staticmethod" para um método estático


p2 = Pessoa.criar_data_nasc(2002, 6,2,"Gabriel")
print(p2.nome,p2.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(17))