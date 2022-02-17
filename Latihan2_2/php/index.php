<?php

include "Product.php";
include "Hardware.php";
include "Memory.php";

$vga1 = new Memory(); // buat objek vga1
// set atribut
$vga1->set_price("Rp. 39.450.000");
$vga1->set_idProduct("N69");
$vga1->set_brand("MSI");
$vga1->set_model("GeForce RTX 3090");
$vga1->set_frequency("19.5 Gbps");
$vga1->set_memorySize("24 GB");
$vga1->set_supportsCuda("10496 Units");

// output untuk vga1
echo "--------------------------------"."<br>";
echo "Price        : ".$vga1->get_price()."<br>";
echo "ID Product   : ".$vga1->get_idProduct()."<br>";
echo "Brand        : ".$vga1->get_brand()."<br>";
echo "Model        : ".$vga1->get_model()."<br>";
echo "Frequency    : ".$vga1->get_frequency()."<br>";
echo "Memory Size  : ".$vga1->get_memorySize()."<br>";
echo "Support Cuda : ".$vga1->get_supportsCuda()."<br>";
echo "--------------------------------"."<br>";

?>