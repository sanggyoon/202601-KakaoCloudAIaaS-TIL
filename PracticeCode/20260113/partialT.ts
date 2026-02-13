type Post = {
  id: number;
  title: string;
  body: string;
};

const post1: Post = { id: 1 }; // compile error, title missing, body missing
const draft: Partial<Post> = {};
draft.title = '임시 제목';
