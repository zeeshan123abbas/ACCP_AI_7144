<?php
// index.php  - run: composer dump-autoload  then  php index.php
require __DIR__ . '/vendor/autoload.php';

use App\Models\{Product, Catalog};

$catalog = (new Catalog())
    ->add(new Product(1, "Wireless Mouse", 2500, 10))
    ->add(new Product(2, "Mechanical Keyboard", 9500, 3))
    ->add(new Product(3, "USB-C Hub", 4200));

foreach ($catalog as $p) {
    echo $p, " | slug: ", $p->slug(), " | with tax: ", $p->priceWithTax(), PHP_EOL;
}
echo "Products: ", count($catalog), ", catalogue value Rs ", number_format($catalog->totalValue()), PHP_EOL;

try {
    $catalog->getIterator()[2]->sell(5);
} catch (RuntimeException $e) {
    echo "Error: ", $e->getMessage(), PHP_EOL;
}
echo "Objects created: ", Product::created(), PHP_EOL;
