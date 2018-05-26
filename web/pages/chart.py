__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2


class chartHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/chart.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/chart.html', chartHandler)
], debug=True)

