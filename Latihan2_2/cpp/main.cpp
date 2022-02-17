#include "Memory.cpp"

int main()
{
    Memory vga1; // buat objek vga1

    // set atribut
    vga1.set_price("Rp. 39.450.000");
    vga1.set_idProduct("N69");
    vga1.set_brand("MSI");
    vga1.set_model("GeForce RTX 3090");
    vga1.set_frequency("19.5 Gbps");
    vga1.set_memorySize("24 GB");
    vga1.set_supportsCuda("10496 Units");

    // output untuk vga1
    cout << "--------------------------------" << endl;
    cout << "Price        : " << vga1.get_price() << endl;
    cout << "ID Product   : " << vga1.get_idProduct() << endl;
    cout << "Brand        : " << vga1.get_brand() << endl;
    cout << "Model        : " << vga1.get_model() << endl;
    cout << "Freqeuency   : " << vga1.get_frequency() << endl;
    cout << "Memory Size  : " << vga1.get_memorySize() << endl;
    cout << "Support Cuda : " << vga1.get_supportsCuda() << endl;
    cout << "--------------------------------" << endl;
    
    return 0;
}