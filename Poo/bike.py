# No python existe a convenção de se utilizar self no lugar do this

from tomlkit import key


class bike:
    def __init__(self,color, model, year, value, gear):
        self.color = color
        self.model = model
        self.year = year
        self.value = value
        self.marcha = gear

    def honk(self):
        print("Plim Plim...")

    def stop(self):
        print("The bike is stopped!")

    def run(self):
        print("The bike is running")

    def change_gear(self, num_gear):
        print("Changing gear")

        def new_gear():
            if num_gear > self.gear:
                print("Gear changed")
            else:
                print("Not possible")

    # def __str__(self):
    #     return f"Bike:\nColor: {self.color}\nModel: {self.model}\nYear: {self.year}\nValue: {self.value}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"
        # Dessa maneira conseguimos retornar o nome da classe, suas propriedas e seus valores   

b1 = bike("Blue","Caloi", 2019,600)
b1.honk()
b1.stop()
b1.run()

b2 = bike("Green","Monark", 2020, 500)
print(b2)