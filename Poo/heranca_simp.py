class veiculo():
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas 

    def ligar_motor(self):
        print("Ligando motor!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

class moto(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self,cor, placa, num_rodas,carregado):
        super().__init__(cor,placa,num_rodas)
        # Com a função super conseguimos "Invocar" metodos da classe pai
        self.carregado = carregado

    def carga(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!")

cam = caminhao("azul", "dsjadsa",4, True)
cam.ligar_motor()
cam.carga()
print(cam)