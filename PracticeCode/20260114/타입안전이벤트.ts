type EventDefinition = {
  [event: string]: any;
};

type MatchEvent<
  Pattern extends string,
  Event extends string
> = Pattern extends "*"
  ? true
  : Pattern extends `${infer Prefix}.*`
  ? Event extends `${Prefix}.${string}`
    ? true
    : false
  : Pattern extends Event
  ? true
  : false;

class TypedEventEmitter<T extends EventDefinition> {
  private handlers = new Map<string, Array<(eventOrData: any, data?: any) => void>>();

  on<K extends keyof T>(event: K, handler: (data: T[K]) => void): () => void;
  on(event: `${string}.*` | "*", handler: (event: string, data: any) => void): () => void;
  on(event: string, handler: Function): () => void {
    if (!this.handlers.has(event)) {
      this.handlers.set(event, []);
    }
    
    this.handlers.get(event)!.push(handler as any);
    
    return () => {
      const handlers = this.handlers.get(event);
      if (handlers) {
        const index = handlers.indexOf(handler as any);
        if (index > -1) {
          handlers.splice(index, 1);
        }
      }
    };
  }

  emit<K extends keyof T>(event: K, data: T[K]): void {
    const eventStr = String(event);
    
    const exactHandlers = this.handlers.get(eventStr);
    if (exactHandlers) {
      exactHandlers.forEach(handler => handler(data));
    }
    
    for (const [pattern, handlers] of this.handlers.entries()) {
      if (pattern !== eventStr) {
        if (pattern === '*' || 
            (pattern.endsWith('.*') && eventStr.startsWith(pattern.slice(0, -2) + '.'))) {
          handlers.forEach(handler => handler(eventStr, data));
        }
      }
    }
  }

  once<K extends keyof T>(event: K, handler: (data: T[K]) => void): () => void {
    let called = false;
    const wrappedHandler = (data: T[K]) => {
      if (!called) {
        called = true;
        handler(data);
        unsubscribe();
      }
    };
    
    const unsubscribe = this.on(event as any, wrappedHandler as any);
    return unsubscribe;
  }
}

type AppEvents = {
  "user.login": { userId: string; timestamp: Date };
  "user.logout": { userId: string };
  "post.create": { postId: string; title: string };
  "post.delete": { postId: string };
};

const emitter = new TypedEventEmitter<AppEvents>();

emitter.on("user.login", (data) => {
  console.log(data.userId);
});

emitter.on("user.*", (event, data) => {
  console.log(event, data);
});

emitter.on("*", (event, data) => {
  console.log(event, data);
});

emitter.emit("user.login", { userId: "123", timestamp: new Date() });

emitter.once("post.create", (data) => {
  console.log(data.postId, data.title);
});