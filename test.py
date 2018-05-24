import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		king=self.request.get('king')
		if(king!=""):
			self.response.write(king + ",You are king!  1")
		else:
			self.response.write("Man,You are king!  1")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)