// post.model.ts - the shape of a post returned by the API
export interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}
