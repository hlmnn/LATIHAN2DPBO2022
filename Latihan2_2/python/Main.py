from Memory import Memory

vga1 = Memory() # buat objek vga1

# set atribut pada object
vga1.set_price("Rp. 39.450.000")
vga1.set_idProduct("N69")
vga1.set_brand("MSI")
vga1.set_model("GeForce RTX 3090")
vga1.set_frequency("19.5 Gbps")
vga1.set_memorySize("24 GB")
vga1.set_supportsCuda("10496 Units")

# output untuk vga1
print(f"--------------------------------")
print(f"Price        : {vga1.get_price()}")
print(f"ID Product   : {vga1.get_idProduct()}")
print(f"Brand        : {vga1.get_brand()}")
print(f"Model        : {vga1.get_model()}")
print(f"Frequency    : {vga1.get_frequency()}")
print(f"Memory Size  : {vga1.get_memorySize()}")
print(f"Support Cuda : {vga1.get_supportsCuda()}")
print(f"--------------------------------")