// class Product adalah parent dari class Hardware
public class Product {
    private String price;
    private String idProduct;
    
    // constructor
    public Product(String price, String idProduct) {
        this.price = price;
        this.idProduct = idProduct;
    }

    // constructor kosong
    public Product() {
    }

    // set product price
    public void set_price(String price) {
        this.price = price;
    }
    // get product price
    public String get_price() {
        return price;
    }

    // set product idProduct
    public void set_idProduct(String idProduct) {
        this.idProduct = idProduct;
    }
    // get product idProduct
    public String get_idProduct() {
        return idProduct;
    }
}