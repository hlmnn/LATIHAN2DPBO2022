// class Hardware adalah child dari class Product dan parent dari class Memory
public class Hardware extends Product {
    private String brand;
    private String model;
    
    // constructor
    public Hardware(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }

    // constructor kosong
    public Hardware() {
    }

    // set memory brand
    public void set_brand(String brand) {
        this.brand = brand;
    }
    // get memory brand
    public String get_brand() {
        return brand;
    }

    // set memory model
    public void set_model(String model) {
        this.model = model;
    }
    // get memory model
    public String get_model() {
        return model;
    }
}