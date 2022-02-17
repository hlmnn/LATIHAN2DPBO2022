<?php

// class Memory adalah child dari class Hardware
class Memory extends Hardware
{
    private $frequency = "";
    private $memorySize = "";
    private $supportsCuda = "";

    //constructor
    function __construct(){
    }

    // set memory frequency
    function set_frequency($frequency)
    {
        $this->frequency = $frequency;
    }
    // get memory frequency
    function get_frequency()
    {
        return $this->frequency;
    }

    // set memory memorySize
    function set_memorySize($memorySize)
    {
        $this->memorySize = $memorySize;
    }
    // get memory memorySize
    function get_memorySize()
    {
        return $this->memorySize;
    }

    // set memory supportsCuda
    function set_supportsCuda($supportsCuda)
    {
        $this->supportsCuda = $supportsCuda;
    }
    // get memory supportsCuda
    function get_supportsCuda()
    {
        return $this->supportsCuda;
    }

    // destructor
    function __destruct(){
    }
}

?>