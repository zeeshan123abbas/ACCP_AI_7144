<?php
// shop.php  (run: php shop.php)
declare(strict_types=1);

interface Shippable { public function shippingCost(string $city): float; }
interface Discountable { public function applyDiscount(float $percent): void; }

abstract class Product
{
    protected static int $created = 0;

    public function __construct(protected string $name, protected float $price)
    {
        static::$created++;
    }

    abstract public function finalPrice(): float;      // children must implement

    public function label(): string                   // shared behaviour
    {
        return sprintf("%-22s Rs %8s", $this->name, number_format($this->finalPrice()));
    }

    final public static function created(): int { return static::$created; }
}

class PhysicalProduct extends Product implements Shippable, Discountable
{
    public function __construct(string $name, float $price, private float $weightKg)
    {
        parent::__construct($name, $price);
    }
    public function finalPrice(): float { return $this->price; }
    public function shippingCost(string $city): float
    {
        $base = $city === 'Karachi' ? 150 : 300;
        return $base + 50 * ceil($this->weightKg);
    }
    public function applyDiscount(float $percent): void { $this->price *= (1 - $percent / 100); }
}

class DigitalProduct extends Product
{
    public function finalPrice(): float { return round($this->price * 1.05, 2); } // 5% digital tax
    public function label(): string { return parent::label() . "  [instant download]"; } // override
}

final class GiftCard extends DigitalProduct
{
    public function finalPrice(): float { return $this->price; }   // no tax on gift cards
}

class Cart
{
    private array $items = [];
    // "overloading" style: accept one or many products
    public function add(Product ...$products): void { array_push($this->items, ...$products); }

    public function __call(string $method, array $args): mixed   // magic method for unknown calls
    {
        if ($method === 'count') return count($this->items);
        throw new BadMethodCallException("Method $method does not exist");
    }

    public function checkout(string $city): void
    {
        $total = 0;
        foreach ($this->items as $p) {
            echo $p->label(), PHP_EOL;                  // polymorphism: each class decides
            $total += $p->finalPrice();
            if ($p instanceof Shippable) $total += $p->shippingCost($city);
        }
        echo str_repeat('-', 50), PHP_EOL, "Total incl. shipping: Rs ", number_format($total), PHP_EOL;
    }
}

$mouse = new PhysicalProduct("Wireless Mouse", 2500, 0.3);
$mouse->applyDiscount(10);
$cart = new Cart();
$cart->add($mouse, new PhysicalProduct("Monitor 24\"", 38000, 4.2), new DigitalProduct("PHP eBook", 1200), new GiftCard("Gift Card", 5000));
echo "Items: ", $cart->count(), PHP_EOL;
$cart->checkout('Lahore');
echo "Products created: ", Product::created(), PHP_EOL;
