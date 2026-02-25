"""
Bluesky Social Network Simulator

This exercise simulates the core behavior of a decentralized
social network similar to Bluesky.

The system supports:
- User registration with unique IDs
- Follow / unfollow functionality
- Post creation with character limit
- Post deletion (only by the author)
- Like / unlike functionality
- Personal feed (latest 10 posts)
- Following feed (latest 10 posts from followed users)
- Error handling for invalid or duplicate actions
"""

from dataclasses import dataclass, field
from datetime import datetime


# ------------------------------------------------------------
# DOMAIN MODELS
# ------------------------------------------------------------

@dataclass
class User:
    """
    Represents a user in the social network.

    Attributes:
        name: Display name of the user.
        id: Unique identifier (assigned by the simulator).
        following: Set of user IDs this user follows.
        followed: Set of user IDs that follow this user.
    """
    name: str
    id: int = 0
    following: set[int] = field(default_factory=set)
    followed: set[int] = field(default_factory=set)

    # Adds a user ID to the following set
    def add_following(self, user_id: int) -> None:
        self.following.add(user_id)

    # Removes a user ID from the following set
    def delete_following(self, user_id: int) -> None:
        self.following.remove(user_id)

    # Registers that another user follows this user
    def add_followed_by(self, user_id: int) -> None:
        self.followed.add(user_id)

    # Removes a follower relationship
    def delete_followed_by(self, user_id: int) -> None:
        self.followed.remove(user_id)


@dataclass
class Post:
    """
    Represents a post created by a user.

    Attributes:
        title: Title of the post.
        author_id: ID of the author user.
        text: Content of the post (max 200 characters).
        id: Unique identifier (assigned by the simulator).
        created_at: Timestamp of creation.
        likes: Set of user IDs who liked the post.
    """
    title: str
    author_id: int
    text: str
    id: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    likes: set[int] = field(default_factory=set)


# ------------------------------------------------------------
# APPLICATION LAYER
# ------------------------------------------------------------

class BlueskySimulator:
    """
    Core application class that manages users, posts,
    relationships, and feed generation.
    """

    def __init__(self) -> None:
        # Auto-increment counters
        self.next_user_id: int = 0
        self.next_post_id: int = 0

        # Storage dictionaries
        self.users: dict[int, User] = {}
        self.posts: dict[int, Post] = {}

    # ------------------------------------------------------------
    # USER MANAGEMENT
    # ------------------------------------------------------------

    def register_user(self, name: str) -> None:
        """
        Registers a new user with a unique auto-incremented ID.
        """
        user = User(name=name, id=self.next_user_id)
        self.users[self.next_user_id] = user
        self.next_user_id += 1

    # ------------------------------------------------------------
    # FOLLOW SYSTEM
    # ------------------------------------------------------------

    def start_following(self, user1_id: int, user2_id: int) -> None:
        """
        Allows one user to follow another.
        Validates existence, self-following, and duplicates.
        """
        if user1_id not in self.users or user2_id not in self.users:
            raise ValueError("One of the users does not exist")

        if user1_id == user2_id:
            raise ValueError("A user cannot follow themselves")

        if user2_id in self.users[user1_id].following:
            raise ValueError("User is already following this account")

        self.users[user1_id].add_following(user2_id)
        self.users[user2_id].add_followed_by(user1_id)

    def stop_following(self, user1_id: int, user2_id: int) -> None:
        """
        Allows one user to unfollow another.
        """
        if user1_id not in self.users or user2_id not in self.users:
            raise ValueError("One of the users does not exist")

        if user1_id == user2_id:
            raise ValueError("A user cannot unfollow themselves")

        if user2_id not in self.users[user1_id].following:
            raise ValueError("User is not following this account")

        self.users[user1_id].delete_following(user2_id)
        self.users[user2_id].delete_followed_by(user1_id)

    # ------------------------------------------------------------
    # POST MANAGEMENT
    # ------------------------------------------------------------

    def create_post(self, user_id: int, title: str, text: str) -> None:
        """
        Creates a post associated with a user.
        Enforces a 200 character limit.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")

        if len(text) > 200:
            raise ValueError("Post text exceeds 200 characters")

        post = Post(
            title=title,
            author_id=user_id,
            text=text,
            id=self.next_post_id
        )

        self.posts[self.next_post_id] = post
        self.next_post_id += 1

    def delete_post(self, user_id: int, post_id: int) -> None:
        """
        Deletes a post if and only if the requesting user
        is the author of the post.
        """
        if post_id not in self.posts:
            raise ValueError("Post does not exist")

        if user_id != self.posts[post_id].author_id:
            raise ValueError("User is not the owner of this post")

        del self.posts[post_id]

    # ------------------------------------------------------------
    # LIKE SYSTEM
    # ------------------------------------------------------------

    def like_post(self, user_id: int, post_id: int) -> None:
        """
        Adds a like from a user to a post.
        Prevents duplicate likes.
        """
        if post_id not in self.posts:
            raise ValueError("Post does not exist")

        if user_id not in self.users:
            raise ValueError("User does not exist")

        if user_id in self.posts[post_id].likes:
            raise ValueError("User has already liked this post")

        self.posts[post_id].likes.add(user_id)

    def unlike_post(self, user_id: int, post_id: int) -> None:
        """
        Removes a like from a post.
        """
        if post_id not in self.posts:
            raise ValueError("Post does not exist")

        if user_id not in self.users:
            raise ValueError("User does not exist")

        if user_id not in self.posts[post_id].likes:
            raise ValueError("User has not liked this post")

        self.posts[post_id].likes.remove(user_id)

    # ------------------------------------------------------------
    # FEED SYSTEM
    # ------------------------------------------------------------

    def feed_user(self, user_id: int) -> None:
        """
        Displays the 10 most recent posts created by the user.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")

        user_posts = [
            post for post in self.posts.values()
            if post.author_id == user_id
        ]

        user_posts.sort(key=lambda x: x.created_at, reverse=True)

        self.print_feeds(user_posts[:10])

    def feed_following(self, user_id: int) -> None:
        """
        Displays the 10 most recent posts from users
        that the given user follows.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")

        feed_following: list[Post] = []

        for followed_id in self.users[user_id].following:
            followed_posts = [
                post for post in self.posts.values()
                if post.author_id == followed_id
            ]
            feed_following.extend(followed_posts)

        feed_following.sort(key=lambda x: x.created_at, reverse=True)

        self.print_feeds(feed_following[:10])

    # ------------------------------------------------------------
    # PRESENTATION LAYER
    # ------------------------------------------------------------

    def print_feeds(self, feeds: list[Post]) -> None:
        """
        Prints formatted post information to the console.
        """
        for feed in feeds:
            print(
                f"Title: {feed.title}\n"
                f"Author Name: {self.users[feed.author_id].name}\n"
                f"Author ID: {feed.author_id}\n"
                f"Created at: {feed.created_at}\n"
                f"Total Likes: {len(feed.likes)}\n"
                f"Text: {feed.text}\n"
            )


# ------------------------------------------------------------
# DEMONSTRATION ENTRY POINT
# ------------------------------------------------------------

def main():
    """
    Demonstrates system behavior:
    - User registration
    - Follow relationships
    - Post creation
    - Likes
    - Feed generation
    - Post deletion
    - Error handling
    """
    app = BlueskySimulator()

    print("=== Registro Usuarios ===")
    app.register_user("Jose")
    app.register_user("Isabel")
    app.register_user("Saúl")

    print("Usuarios registrados:")
    for user_id, user in app.users.items():
        print(f"ID: {user_id} | Name: {user.name}")
    print()

    print("=== Followers ===")
    app.start_following(0, 1)
    app.start_following(0, 2)
    app.start_following(1, 2)

    print("Jose sigue:", app.users[0].following)
    print("Isabel follows:", app.users[1].following)
    print()

    print("=== Creacion de POSTS ===")
    app.create_post(1, " Post de Isabel", "Hola, soy Isabel!")
    app.create_post(2, "Primer Post de Saúl", "Este es mi primer post.")
    app.create_post(2, "Segundo Post de Saúl", "Este es mi segundo post.")
    app.create_post(0, "Post de Jose",
                    "Mi primer post en el simulador de Bluesky.")
    print()

    print("=== LIKES ===")
    app.like_post(0, 0)
    app.like_post(0, 1)
    app.like_post(1, 1)
    print()

    print("=== FEEDs de Saúl ===")
    app.feed_user(2)
    print()

    print("=== FEEDs de los que sigue Jose ===")
    app.feed_following(0)
    print()

    print("=== Borrado de POST ===")
    app.delete_post(1, 0)
    print()

    print("=== Gestion de ERRORES ===")
    try:
        app.start_following(0, 1)
    except ValueError as e:
        print("Handled error:", e)


if __name__ == "__main__":
    main()
