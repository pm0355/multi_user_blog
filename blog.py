from webapp2 import WSGIApplication
from google.appengine.ext import db
from helpers import *


# Models
from models.user import User
from models.post import Post



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

app = WSGIApplication([
                               ('/blog/?', BlogFrontHandler),
                               ('/blog/([0-9]+)', PostHandler),
                               ('/blog/editpost/([0-9]+)', EditPostHandler),
                               ('/blog/deletepost/([0-9]+)', DeletePostHandler),
                               ('/blog/newpost', NewPostHandler),
                               ('/signup', SignupHandler),
                               ('/login', LoginHandler),
                               ('/logout', LogoutHandler),
                               ],
                              debug=True)
