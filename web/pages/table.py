__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2
from models.user import User


class TableHandler(webapp2.RequestHandler):
    def get(self):
		template_params = {}
		html = template.render("web/table.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
    ('/table.html', TableHandler)
], debug=True)

