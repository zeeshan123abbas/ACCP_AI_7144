<?php
namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StorePostRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true;   // Session 08 restricts this to logged-in users
    }

    public function rules(): array
    {
        return [
            'title'        => ['required', 'string', 'min:5', 'max:150'],
            'body'         => ['required', 'string', 'min:20'],
            'category_id'  => ['nullable', 'exists:categories,id'],
            'is_published' => ['boolean'],
        ];
    }

    protected function prepareForValidation(): void
    {
        $this->merge(['is_published' => $this->boolean('is_published')]);
    }

    public function messages(): array
    {
        return ['body.min' => 'Please write at least 20 characters.'];
    }
}
