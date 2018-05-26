__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2


class formHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/form.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/form.html', formHandler)
], debug=True)

