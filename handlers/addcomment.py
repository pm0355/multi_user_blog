
from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *
from models.comment import Comment

class AddCommentHandler(BlogHandler):

    def get(self, post_id):
        if not self.user:
            self.render('/login')
        else:
            self.render("addcomment.html")

    def post(self, post_id):
        if not self.user:
            return

        content = self.request.get('content')

        user_name = self.user.name
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())

        c = Comment(parent=key, user_id=int(self.user.key().id()), content=content, user_name=user_name)
        c.put()
        
        self.redirect('/blog/%s' % str(p.key().id()))

        # melinda and hari patel mark sterit 2:30pm