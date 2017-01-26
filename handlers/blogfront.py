from google.appengine.ext import db
from handlers.blog import BlogHandler

class BlogFrontHandler(BlogHandler):
    def get(self):
        posts = greetings = Post.all().order('-created')
        self.render('front.html', posts = posts)