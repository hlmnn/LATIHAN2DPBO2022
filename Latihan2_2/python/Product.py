# class Product adalah parent dari class Hardware
class Product:
    # constructor
    def __init__(self):
        self.price = ""
        self.idProduct = ""
    
    # set product price
    def set_price(self, price):
        self.price = price
    # get product price
    def get_price(self):
        return self.price

    # set product price
    def set_idProduct(self, idProduct):
        self.idProduct = idProduct
    # get product price
    def get_idProduct(self):
        return self.idProduct