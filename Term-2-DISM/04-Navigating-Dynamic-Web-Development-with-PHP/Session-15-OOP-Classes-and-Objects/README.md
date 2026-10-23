# Session 15: Object-Oriented PHP: Classes and Objects

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain OOP concepts: class, object, property, method
- Write constructors (with property promotion) and destructors
- Use $this, typed properties and readonly properties
- Organise classes with namespaces and Composer autoloading
- Reuse code with traits and iterate objects

## 📖 Concepts Explained

### 1. Why OOP?

Procedural code groups **functions**; object-oriented code groups **data + behaviour** into objects that model real things (Product, Cart, Student). Benefits: organisation, reuse, easier testing and teamwork. Laravel is completely object-oriented.

| Term | Meaning | Example |
|---|---|---|
| Class | blueprint | `class Product` |
| Object | instance created from a class | `$p = new Product(...)` |
| Property | variable inside a class | `$price` |
| Method | function inside a class | `priceWithTax()` |
| Constructor | runs on `new` | `__construct()` |
| Destructor | runs when object is destroyed | `__destruct()` |

### 2. Constructor property promotion (PHP 8)

```php
class Product {
    public function __construct(
        public readonly string $name,
        private float $price,
    ) {}
}
```

Declares, types and assigns properties in one place. `readonly` (8.1) can be set once only.

### 3. Namespaces and autoloading

Namespaces avoid name clashes (`App\Models\Product` vs a library's `Product`). With Composer's **PSR-4** autoloading, `App\` maps to `src/`, and classes load automatically when first used — no more long lists of `require`.

### 4. Traits

A **trait** is a set of methods you can paste into several unrelated classes (`use HasSlug;`) — horizontal reuse, since PHP has single inheritance.

### 5. Iterables

Implement `IteratorAggregate` so an object can be used in `foreach`, or use `iterable` type hints for anything loopable.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Product class (`src/Models/Product.php`)

```php
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
```

**How it works:**

- Promoted constructor parameters become properties automatically.
- `$price` is private: it can be read via `price()` but changed only through class rules.
- `self::$count` is shared by all objects (static).
- `__toString()` decides how the object prints with `echo`.

### Example 2: A reusable trait (`src/Traits/HasSlug.php`)

```php
<?php
// src/Traits/HasSlug.php
namespace App\Traits;

trait HasSlug
{
    public function slug(): string
    {
        $s = strtolower(trim(preg_replace('/[^A-Za-z0-9]+/', '-', $this->name), '-'));
        return $s;
    }
}
```

**How it works:**

Any class with a `name` property that `use`s this trait gets a `slug()` method (e.g. `wireless-mouse`).

### Example 3: An iterable collection (`src/Models/Catalog.php`)

```php
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
```

**How it works:**

`IteratorAggregate` makes `foreach ($catalog as $p)` work; `Countable` makes `count($catalog)` work. Returning `static` allows chaining.

### Example 4: Using the classes (`index.php`)

```php
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
```

**How it works:**

Composer's autoloader loads each class from `src/` the first time it is used.

### Example 5: PSR-4 autoload mapping (`composer.json`)

```json
{
    "autoload": {
        "psr-4": { "App\\": "src/" }
    }
}
```

**How it works:**

Run `composer dump-autoload` once to generate `vendor/autoload.php`.

## 🧪 Lab Practice

1. Run `composer dump-autoload` and `php index.php`.
2. Add a `discount(float $percent)` method that returns a new price without changing the original.
3. Create a `Student` class with promoted properties and a `__toString()`.
4. Create a `HasTimestamps` trait with `createdAt()` and use it in two classes.
5. Try to change a `readonly` property and read the error.

## 📝 Assignment

Model a **Book Shop**: classes `Book` (isbn, title, author, price, stock) and `Inventory` (add, remove, find by isbn, total value, low-stock list) in namespace `App\Shop`, autoloaded with Composer, plus a script that demonstrates every method.

## ❓ Quick Quiz

1. What runs automatically when you use `new`?
   - a) __toString
   - b) __construct
   - c) __destruct
   - d) __get
2. What does readonly mean on a property?
3. Why use namespaces?
4. What is a trait?
5. How do you access a static property inside its class?

<details>
<summary>Show answers</summary>

1. b) __construct
2. It can be assigned only once (normally in the constructor).
3. To group classes and avoid name collisions.
4. A reusable set of methods inserted into classes with `use`.
5. `self::$name` (or `static::$name`).

</details>

## 💼 Interview Questions

1. **Explain the four pillars of OOP.**

   <details><summary>Model answer</summary>

   Encapsulation (hide internal state), Abstraction (expose simple interfaces), Inheritance (reuse via parent classes), Polymorphism (one interface, many implementations).

   </details>

2. **What is PSR-4 autoloading?**

   <details><summary>Model answer</summary>

   A standard mapping namespaces to folder paths so an autoloader can find class files automatically, e.g. App\Models\Product → src/Models/Product.php.

   </details>

3. **Trait vs inheritance?**

   <details><summary>Model answer</summary>

   Inheritance creates an is-a relationship with one parent; traits copy methods into any class for horizontal reuse without a type relationship.

   </details>

## ✅ Summary

- Classes are blueprints; objects are instances.
- Constructor promotion and readonly make classes short and safe.
- Namespaces + Composer PSR-4 autoloading organise code.
- Traits share methods; IteratorAggregate makes objects loopable.

---

[⬅ Previous](../Session-14-Authentication-and-Authorization/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-16-OOP-Inheritance-Interfaces/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
