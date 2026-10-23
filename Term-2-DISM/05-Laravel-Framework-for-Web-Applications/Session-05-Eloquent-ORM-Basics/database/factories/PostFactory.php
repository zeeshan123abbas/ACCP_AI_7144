<?php
namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

class PostFactory extends Factory
{
    public function definition(): array
    {
        return [
            'title'        => fake()->sentence(6),
            'body'         => fake()->paragraphs(3, true),
            'is_published' => fake()->boolean(70),
        ];
    }
}
