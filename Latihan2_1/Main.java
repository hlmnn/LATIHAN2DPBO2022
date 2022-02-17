public class Main {
    public static void main(String[] args) {
        Memory vga1 = new Memory(); // buat objek vga1

        // set atribut
        vga1.set_price("Rp. 39.450.000");
        vga1.set_idProduct("N69");
        vga1.set_brand("MSI");
        vga1.set_model("GeForce RTX 3090");
        vga1.set_frequency("19.5 Gbps");
        vga1.set_memorySize("24 GB");
        vga1.set_supportsCuda("10496 Units");

        // output untuk vga1
        System.out.println("--------------------------------");
        System.out.println("Price        : " + vga1.get_price());
        System.out.println("ID Product   : " + vga1.get_idProduct());
        System.out.println("Brand        : " + vga1.get_brand());
        System.out.println("Model        : " + vga1.get_model());
        System.out.println("Frequency    : " + vga1.get_frequency());
        System.out.println("Memory Size  : " + vga1.get_memorySize());
        System.out.println("Support Cuda : " + vga1.get_supportsCuda());
        System.out.println("--------------------------------");
    }
}