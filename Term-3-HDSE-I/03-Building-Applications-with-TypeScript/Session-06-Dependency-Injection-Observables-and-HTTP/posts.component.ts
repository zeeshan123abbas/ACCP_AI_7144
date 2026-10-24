// posts.component.ts - uses the service and shows loading / error states
import { Component, OnInit, inject } from '@angular/core';
import { PostService } from './post.service';
import { Post } from './post.model';

@Component({
  selector: 'app-posts',
  standalone: true,
  template: `
    <h2>Latest Posts</h2>
    <button (click)="createPost()">Add a test post</button>

    @if (loading) {
      <p>Loading...</p>
    } @else if (errorMessage) {
      <p style="color: red">{{ errorMessage }}</p>
    } @else {
      <ol>
        @for (post of posts; track post.id) {
          <li><strong>{{ post.title }}</strong></li>
        }
      </ol>
    }
  `,
})
export class PostsComponent implements OnInit {
  private postService = inject(PostService);
  posts: Post[] = [];
  loading = true;
  errorMessage = '';

  ngOnInit(): void {
    // Nothing happens until we subscribe
    this.postService.getPosts().subscribe({
      next: (data) => {
        this.posts = data;
        this.loading = false;
      },
      error: () => {
        this.errorMessage = 'Could not load posts. Check your internet.';
        this.loading = false;
      },
    });
  }

  createPost(): void {
    this.postService.addPost('My Angular post').subscribe((saved) => {
      // the fake API returns the post with a new id (101)
      this.posts = [saved, ...this.posts];
    });
  }
}
