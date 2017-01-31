
from handlers.blog import BlogHandler
from models.post import Post
from helpers import *

class DeletePostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user.key().id() == post.user_id:
            post.delete()
            self.render('front.html')
        elif not self.user:
            self.redirect("/login")
        else:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            comments = db.GqlQuery(
                "select * from Comment where ancestor is :1 order by created desc limit 10", key)

            error = "You don't have permission to delete this post"
            self.render("permalink.html", post=post, comments=comments, error=error)



#http://localhost:8080/blog/editpost/5066549580791808
