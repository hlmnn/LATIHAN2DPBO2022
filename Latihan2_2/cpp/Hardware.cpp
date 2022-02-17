#include "Product.cpp"

// class Hardware adalah child dari class Product dan parent dari class Memory
class Hardware: public Product
{   
    // atribut private
    private:
        string brand;
        string model;
            
    public:
        // constructor 
        Hardware(string brand, string model) {
            this->brand = brand;
            this->model = model;
        }

        // constructor kosong
        Hardware() {
        }

        // set hardware brand
        void set_brand(string brand) {
            this->brand = brand;
        }
        // get hardware brand
         string get_brand() {
            return this->brand;
        }

        // set hardware model
        void set_model(string model) {
            this->model = model;
        }
        // get hardware model
        string get_model() {
            return this->model;
        }

        // destructor
        ~Hardware() {
        }
};