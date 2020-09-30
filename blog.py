class Blog:
    def __init__(self, title, author,posts):
        self.title = title
        self.author = author
        self.posts = posts

    def __repr__(self):
        return self.title + ' por ' + self.author + ' (' + str(len(self.posts)) + ' post' + ('s)' if len(self.posts) != 1 else ')')