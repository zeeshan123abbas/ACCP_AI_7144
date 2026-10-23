<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        Schema::table('users', fn (Blueprint $t) => $t->string('role')->default('user')->after('email'));
        Schema::table('posts', fn (Blueprint $t) => $t->foreignId('user_id')->nullable()->constrained()->cascadeOnDelete());
    }
    public function down(): void
    {
        Schema::table('posts', fn (Blueprint $t) => $t->dropConstrainedForeignId('user_id'));
        Schema::table('users', fn (Blueprint $t) => $t->dropColumn('role'));
    }
};
