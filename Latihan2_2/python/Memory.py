from Hardware import Hardware

# class Memory adalah child dari class Hardware
class Memory(Hardware):
    # constructor
    def __init__(self):
        self.frequency = ""
        self.memorySize = ""
        self.supportsCuda = ""

    # set memory frequency
    def set_frequency(self, frequency):
        self.frequency = frequency
    # set memory frequency
    def get_frequency(self):
        return self.frequency

    # set memory memorySize
    def set_memorySize(self, memorySize):
        self.memorySize = memorySize
    # set memory memorySize
    def get_memorySize(self):
        return self.memorySize

    # set memory supportsCuda
    def set_supportsCuda(self, supportsCuda):
        self.supportsCuda = supportsCuda
    # set memory supportsCuda
    def get_supportsCuda(self):
        return self.supportsCuda