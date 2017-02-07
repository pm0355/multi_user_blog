
from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *
from models.comment import Comment

class EditCommentHandler(BlogHandler):

    def get(self, post_id, comment_id):
        post_key= db.Key.from_path('Post', int(post_id),parent= blog_key())
        post= db.get(post_key)

        comment_key= db.Key.from_path('Comment', int(comment_id), parent=post_key)
        comment = db.get(comment_key)

        if not self.user:
            self.render('/login')
        else:
            self.render("editcomment.html", content=comment.content)

    def post(self, post_id, comment_id):

        post_key= db.Key.from_path('Post', int(post_id),parent= blog_key())
        post= db.get(post_key)

        comment_key= db.Key.from_path('Comment', int(comment_id), parent=post_key)
        comment = db.get(comment_key)
        
        if not self.user:
            self.redirect('/blog')

        if self.user.key().id() == post.user_id:
            content = self.request.get('content')
            user_name = self.user.name
            if content:
                c = Comment(parent=comment_key, user_id=int(self.user.key().id()), content=content, user_name=user_name)
                c.put()
        
                self.redirect('/blog/%s' % str(post_id))
