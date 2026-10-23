<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        Schema::create('categories', function (Blueprint $t) {
            $t->id(); $t->string('name')->unique(); $t->timestamps();
        });
        Schema::table('posts', function (Blueprint $t) {
            $t->foreignId('category_id')->nullable()->constrained()->nullOnDelete();
            $t->string('slug')->nullable()->unique();
            $t->softDeletes();
        });
        Schema::create('tags', function (Blueprint $t) {
            $t->id(); $t->string('name')->unique(); $t->timestamps();
        });
        Schema::create('post_tag', function (Blueprint $t) {
            $t->foreignId('post_id')->constrained()->cascadeOnDelete();
            $t->foreignId('tag_id')->constrained()->cascadeOnDelete();
            $t->primary(['post_id', 'tag_id']);
        });
    }
    public function down(): void
    {
        Schema::dropIfExists('post_tag');
        Schema::dropIfExists('tags');
        Schema::table('posts', function (Blueprint $t) {
            $t->dropConstrainedForeignId('category_id');
            $t->dropColumn(['slug', 'deleted_at']);
        });
        Schema::dropIfExists('categories');
    }
};
