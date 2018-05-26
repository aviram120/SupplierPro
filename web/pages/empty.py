__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2


class emptyHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/empty.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/empty.html', emptyHandler)
], debug=True)

