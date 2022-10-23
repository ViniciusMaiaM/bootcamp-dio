class Aluno:
    escola = "UFRN"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostra_valor(*objs):
    for obj in objs:
        print(obj)

est_1 = Aluno("Estudante",1)
est_2 = Aluno("Estudante2",2)

mostra_valor(est_1,est_2)

est_1.matricula = 3 #Aqui modifica-se apenas a variavel deste objeto

mostra_valor(est_1,est_2)

Aluno.escola = "Python" #Aqui modificamos para todos os objetos criados com base na classe

mostra_valor(est_1,est_2)
#Variaveis de classe são unicas pra todos os objetos