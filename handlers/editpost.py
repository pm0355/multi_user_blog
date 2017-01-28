
from handlers.blog import BlogHandler
from models.post import Post
from helpers import *

class EditPostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user:
            self.render("editpost.html",subject=post.subject,content=post.content,post_id=post_id)
        else:
            self.redirect("/login")

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not self.user:
            self.redirect('/blog')

            subject = self.request.get('subject')
            content = self.request.get('content')

            if subject and content:
                post.put()
                self.redirect('/blog/%s' % str(post.key().id()))
            else:
                error = "subject and content, please!"
                self.render("editpost.html", subject=subject, content=content, error=error)

#http://localhost:8080/blog/editpost/5066549580791808
