<?php
// src/Models/Catalog.php
namespace App\Models;

class Catalog implements \IteratorAggregate, \Countable
{
    /** @var Product[] */
    private array $items = [];

    public function add(Product $p): static { $this->items[$p->id] = $p; return $this; }
    public function getIterator(): \ArrayIterator { return new \ArrayIterator($this->items); }
    public function count(): int { return count($this->items); }
    public function totalValue(): float
    {
        return array_sum(array_map(fn(Product $p) => $p->price(), $this->items));
    }
}
