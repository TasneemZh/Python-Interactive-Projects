import requests


class Post:
    def __init__(self):
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
        self.posts = response.json()

    def fetch_posts(self):
        return self.posts

    def fetch_post(self, post_id):
        for post in self.posts:
            if post["id"] == post_id:
                return post
