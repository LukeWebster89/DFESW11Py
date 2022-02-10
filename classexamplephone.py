class Phone:

    def __init__(self, make, model, colour, memory, price):
        self.make = make
        self.model = model
        self.colour = colour
        self.memory = memory
        self.price = price

    def make_and_model(self):
        return self.make, self.model


myphone = Phone("Samsung", "Galaxy S21 Ultra", "Black", "128GB", 1149 )      

print(myphone.make_and_model())
