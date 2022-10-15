# No python existe a convenção de se utilizar self no lugar do this

class bike:
    def __init__(self,color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def honk(self):
        print("Plim Plim...")

    def stop(self):
        print("The bike is stopped!")

    def run(self):
        print("The bike is running")


b1 = bike("Blue","Caloi",2019,600)
b1.honk()
b1.stop()
b1.run()