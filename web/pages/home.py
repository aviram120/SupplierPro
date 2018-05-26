__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/index.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/index.html', IndexHandler)
], debug=True)

