from webapp2 import WSGIApplication
from google.appengine.ext import db
from helpers import *


# Models
from models.user import User
from models.post import Post
from models.like import Like


# Handlers
from handlers.blog import BlogHandler
from handlers.blogfront import BlogFrontHandler
from handlers.signup import SignupHandler
from handlers.login import LoginHandler
from handlers.logout import LogoutHandler
from handlers.post import PostHandler
from handlers.newpost import NewPostHandler
from handlers.editpost import EditPostHandler
from handlers.deletepost import DeletePostHandler
from handlers.likepost import LikePostHandler
from handlers.addcomment import AddCommentHandler
from handlers.editcomment import EditCommentHandler

app = WSGIApplication([
                               ('/blog/?', BlogFrontHandler),
                               ('/blog/([0-9]+)', PostHandler),
                               ('/blog/editpost/([0-9]+)', EditPostHandler),
                               ('/blog/deletepost/([0-9]+)', DeletePostHandler),
                               ('/blog/newpost', NewPostHandler),
                               ('/blog/like/([0-9]+)', LikePostHandler),
                               ('/blog/addcomment/([0-9]+)',AddCommentHandler),
                               ('/blog/editcomment/([0-9]+)',EditCommentHandler),
                               ('/signup', SignupHandler),
                               ('/login', LoginHandler),
                               ('/logout', LogoutHandler),
                               ],
                              debug=True)
