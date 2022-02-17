from Hardware import Hardware

# class Memory adalah child dari class Hardware
class Memory(Hardware):
    # atribut private
    __frequency = ""
    __memorySize = ""
    __supportsCuda = ""

    # constructor
    def __init__(self):
        self.__frequency = ""
        self.__memorySize = ""
        self.supportsCuda = ""

    # set memory frequency
    def set_frequency(self, frequency):
        self.__frequency = frequency
    # set memory frequency
    def get_frequency(self):
        return self.__frequency

    # set memory memorySize
    def set_memorySize(self, memorySize):
        self.__memorySize = memorySize
    # set memory memorySize
    def get_memorySize(self):
        return self.__memorySize

    # set memory supportsCuda
    def set_supportsCuda(self, supportsCuda):
        self.__supportsCuda = supportsCuda
    # set memory supportsCuda
    def get_supportsCuda(self):
        return self.__supportsCuda