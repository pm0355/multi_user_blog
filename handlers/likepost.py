
from handlers.blog import BlogHandler
from models.post import Post
from models.like import Like
from helpers import *

class LikePostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user.key().id() == post.user_id:
            error="Sorry, you cannot like your own post."
            self.write(error)
        elif not self.user:
        	self.redirect('/login')
        else:
        	user_id = self.user.key()
        	post_id= post.key().id()
        	like = Like.all().filter('user_id=',user_id).filter('post_id=',post_id).get()

        	if like:
        		self.redirect('/blog/%s' % str(post.key().id()))
        	else:
        		like = Like(parent=key, user_id=self.user.key().id(), post_id= post.key().id())
        		post.likes +=1
        		like.put()
        		post.put()
        		self.redirect('/blog/%s' % str(post.key().id()))