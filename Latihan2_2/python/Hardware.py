from Product import Product

# class Hardware adalah child dari class Product dan parent dari class Memory
class Hardware(Product):
    # constructor
    def __init__(self):
        self.brand = ""
        self.model = ""
    
    # set hardware brand
    def set_brand(self, brand):
        self.brand = brand
    # get hardware brand
    def get_brand(self):
        return self.brand
    
    # set hardware model
    def set_model(self, model):
        self.model = model
    # get hardware model
    def get_model(self):
        return self.model