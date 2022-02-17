<?php

// class Product adalah parent dari class Hardware
class Product
{
    private $price = "";
    private $idProduct = "";

    //constructor
    function __construct(){
    }

    // set memory price
    function set_price($price)
    {
        $this->price = $price;
    }
    // get memory price
    function get_price()
    {
        return $this->price;
    }

    // set memory idProduct
    function set_idProduct($idProduct)
    {
        $this->idProduct = $idProduct;
    }
    // get memory idProduct
    function get_idProduct()
    {
        return $this->idProduct;
    }

    // destructor
    function __destruct(){
    }
}

?>