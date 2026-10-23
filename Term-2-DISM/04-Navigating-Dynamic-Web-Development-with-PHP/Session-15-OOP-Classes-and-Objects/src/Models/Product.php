<?php
// src/Models/Product.php
declare(strict_types=1);
namespace App\Models;

use App\Traits\HasSlug;

class Product
{
    use HasSlug;

    private static int $count = 0;
    public const TAX_RATE = 0.17;

    public function __construct(
        public readonly int $id,
        public readonly string $name,
        private float $price,
        private int $stock = 0,
    ) {
        if ($price < 0) throw new \InvalidArgumentException("Price cannot be negative");
        self::$count++;
    }

    public function price(): float { return $this->price; }
    public function priceWithTax(): float { return round($this->price * (1 + self::TAX_RATE), 2); }
    public function inStock(): bool { return $this->stock > 0; }

    public function sell(int $qty = 1): void
    {
        if ($qty > $this->stock) throw new \RuntimeException("Only {$this->stock} left of {$this->name}");
        $this->stock -= $qty;
    }

    public static function created(): int { return self::$count; }

    public function __toString(): string
    {
        return sprintf("#%d %s - Rs %s (%d in stock)", $this->id, $this->name, number_format($this->price), $this->stock);
    }

    public function __destruct() { /* e.g. release resources */ }
}
