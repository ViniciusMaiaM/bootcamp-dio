class Pessoa:
    def __init__(self,nome, ano_nasc):
        self.nome = nome
        self._ano_nasc = ano_nasc
    
    @property
    def idade(self):
        _ano_atual = 2022 #Assim não se deve alterar a variavel
        return _ano_atual - self._ano_nasc

pes = Pessoa("Teste",2000)
print(f"Nome: {pes.nome}\tIdade: {pes.idade}")

#Caso o objeto ou a característica pode ser moficada e não precisa ser protegida
#não existe necessidade de se criar uma propriedade ou "proteger" a tal