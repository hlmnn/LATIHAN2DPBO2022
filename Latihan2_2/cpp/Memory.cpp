#include "Hardware.cpp"

// class Memory adalah child dari class Hardware
class Memory: public Hardware
{
    // atribut private
    private:
        string frequency;
        string memorySize;
        string supportsCuda;
        
    public:
        // constructor
        Memory(string frequency, string memorySize, string supportsCuda) {
            this->frequency = frequency;
            this->memorySize = memorySize;
            this->supportsCuda = supportsCuda;
        }

        // constructor kosong
        Memory() {
        }

        // set memory frequency
        void set_frequency(string frequency) {
            this->frequency = frequency;
        }
        // get memory frequency
        string get_frequency() {
            return this->frequency;
        }

        // set memory memorySize
        void set_memorySize(string memorySize) {
            this->memorySize = memorySize;
        }
        // get memory memorySize
        string get_memorySize() {
            return this->memorySize;
        }
        
        // set memory SupportCuda
        void set_supportsCuda(string supportsCuda) {
            this->supportsCuda = supportsCuda;
        }
        // get memory supportCuda
        string get_supportsCuda() {
            return this->supportsCuda;
        }

        // destructor
        ~Memory() {
        }
};