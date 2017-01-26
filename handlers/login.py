from handlers.blog import BlogHandler
from models.user import User


class LoginHandler(BlogHandler):
    def get(self):
        self.render('login-form.html')