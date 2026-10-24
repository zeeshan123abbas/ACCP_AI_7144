// post.service.ts - all HTTP calls for posts live here
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Post } from './post.model';

@Injectable({ providedIn: 'root' })
export class PostService {
  private http = inject(HttpClient);
  private apiUrl = 'https://jsonplaceholder.typicode.com/posts';

  // GET: returns an Observable that will deliver an array of posts
  getPosts(): Observable<Post[]> {
    return this.http.get<Post[]>(this.apiUrl + '?_limit=5');
  }

  // POST: send a new post to the server
  addPost(title: string): Observable<Post> {
    const newPost = { title: title, body: 'Created from Angular', userId: 1 };
    return this.http.post<Post>(this.apiUrl, newPost);
  }
}
