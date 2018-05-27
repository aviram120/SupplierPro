__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2
from models.user import User


class insertUserHandler(webapp2.RequestHandler):
    def get(self):
		maildb = self.request.get('mail')
		passworddb = self.request.get('pwd')
		usernamedb = self.request.get('userName')
		usercode = 45
		
		user = User(username=usernamedb, mail=maildb,user_code=usercode)
		user.set_password(passworddb)
		user.put()
		self.post("add user to Db - user: " + usernamedb +" , maildb: " + maildb)

		
    def post(self,response):
		self.response.write(response)
		
		

app = webapp2.WSGIApplication([
    ('/insertUser', insertUserHandler)
], debug=True)

