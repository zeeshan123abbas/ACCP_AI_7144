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
