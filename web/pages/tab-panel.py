__author__ = 'Yaacov&Aviram'

from google.appengine.ext.webapp import template
import webapp2


class tabpanelHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/tab-panel.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/tab-panel.html', tabpanelHandler)
], debug=True)

