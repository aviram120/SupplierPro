__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2


class uielementsHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/ui-elements.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/ui-elements.html', uielementsHandler)
], debug=True)

