<?php

// class Hardware adalah child dari class Product dan parent dari class Memory
class Hardware extends Product
{
    private $brand = "";
    private $model = "";

    //constructor
    function __construct(){
    }

    // set memory brand
    function set_brand($brand)
    {
        $this->brand = $brand;
    }
    // get memory brand
    function get_brand()
    {
        return $this->brand;
    }

    // set memory model
    function set_model($model)
    {
        $this->model = $model;
    }
    // get memory model
    function get_model()
    {
        return $this->model;
    }

    // destructor
    function __destruct(){
    }
}

?>