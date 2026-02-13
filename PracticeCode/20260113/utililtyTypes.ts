type User3 = {
  id: number;
  name: string;
  email: string;
};

type UserPreview = Pick<User3, 'id' | 'name'>;
//{ id: number; name: string; }

type UserPreview2 = Omit<User3, 'id' | 'name'>;
//{ email: string; }

type Status = 'idle' | 'loading' | 'success' | 'error';

type ActiveStatus = Exclude<Status, 'idle' | 'error'>;
// "loading" | "success"

type CommonStatus = Extract<Status, 'loading' | 'error'>;
// "loading" | "error"
