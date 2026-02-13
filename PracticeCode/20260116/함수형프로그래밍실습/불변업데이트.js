const state = {
  user: {
    profile: {
      name: 'Kim',
      email: 'kim@test.com',
    },
    settings: {
      theme: 'dark',
      notifications: {
        email: true,
        push: false,
      },
    },
  },
  posts: [
    { id: 1, title: 'Hello', likes: 10 },
    { id: 2, title: 'World', likes: 20 },
  ],
};

//TODO: 다음 함수들을 구현하세요

function updateUserName(state, newName) {
  // user.profile.name 업데이트
  return {
    ...state,
    user: {
      ...state.user,
      profile: {
        ...state.user.profile,
        name: newName,
      },
    },
  };
}

function togglePushNotification(state) {
  // user.settings.notifications.push 토글
  return {
    ...state,
    user: {
      ...state.user,
      settings: {
        ...state.user.settings,
        notifications: {
          ...state.user.settings.notifications,
          push: state.user.settings.notifications.push ? false : true,
        },
      },
    },
  };
}

function incrementPostLikes(state, postId) {
  // 특정 post의 likes 증가
  return {
    ...state,
    posts: state.posts.map((post) => {
      if (post.id === postId) {
        return {
          ...post,
          likes: post.likes + 1,
        };
      } else {
        return {
          ...post,
        };
      }
    }),
  };
}

function addPost(state, newPost) {
  // posts 배열에 새 포스트 추가
  return {
    ...state,
    posts: [...state.posts, newPost],
  };
}

// 테스트
const s1 = updateUserName(state, 'Lee');
console.log(s1.user.profile.name); // 'Lee'
console.log(state.user.profile.name); // 'Kim' (원본 유지)

const s2 = togglePushNotification(state);
console.log(s2.user.settings.notifications.push); // true

const s3 = incrementPostLikes(state, 1);
console.log(s3.posts[0].likes); // 11

const s4 = addPost(state, { id: 3, title: 'New', likes: 0 });
console.log(s4.posts.length); // 3
