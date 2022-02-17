# class Product adalah parent dari class Hardware
class Product:
    # atribut private
    __price = ""
    __idProduct = ""

    # constructor
    def __init__(self):
        self.__price = ""
        self.__idProduct = ""
    
    # set product price
    def set_price(self, price):
        self.__price = price
    # get product price
    def get_price(self):
        return self.__price

    # set product price
    def set_idProduct(self, idProduct):
        self.__idProduct = idProduct
    # get product price
    def get_idProduct(self):
        return self.__idProduct