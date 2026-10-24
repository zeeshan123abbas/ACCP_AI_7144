// task.model.ts - the shape of one task (an interface in its own file)
export interface Task {
  id: number;
  title: string;
  priority: 'low' | 'medium' | 'high'; // only these three words are allowed
  done: boolean;
}
