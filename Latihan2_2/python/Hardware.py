from Product import Product

# class Hardware adalah child dari class Product dan parent dari class Memory
class Hardware(Product):
    # atribut private
    __brand = ""
    __model = ""

    # constructor
    def __init__(self):
        self.__brand = ""
        self.__model = ""
    
    # set hardware brand
    def set_brand(self, brand):
        self.__brand = brand
    # get hardware brand
    def get_brand(self):
        return self.__brand
    
    # set hardware model
    def set_model(self, model):
        self.__model = model
    # get hardware model
    def get_model(self):
        return self.__model