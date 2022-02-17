// class Memory adalah child dari class Hardware
public class Memory extends Hardware {
    private String frequency;
    private String memorySize;
    private String supportsCuda;
    
    // constructor
    public Memory(String frequency, String memorySize, String supportsCuda) {
        this.frequency = frequency;
        this.memorySize = memorySize;
        this.supportsCuda = supportsCuda;
    }

    // constructor kosong
    public Memory() {
    }

    // set memory frequency
    public void set_frequency(String frequency) {
        this.frequency = frequency;
    }
    // get memory frequency
    public String get_frequency() {
        return frequency;
    }

    // set memory memorySize
    public void set_memorySize(String memorySize) {
        this.memorySize = memorySize;
    }
    // get memory memorySize
    public String get_memorySize() {
        return memorySize;
    }

    // set memory supportsCuda
    public void set_supportsCuda(String supportsCuda) {
        this.supportsCuda = supportsCuda;
    }
    // get memory supportsCuda
    public String get_supportsCuda() {
        return supportsCuda;
    }
}