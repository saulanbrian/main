class Post:

    def __init__(self, content):
        self.id = content["id"]
        self.title = content["title"]
        self.subtitle = content["subtitle"]
        self.body = content["body"]