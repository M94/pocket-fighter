import os
import webapp2

from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), 'app/' + templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class MainPage(webapp2.RequestHandler):
	def get(self): 
		welcome_msg = 'Welcome to Pocket Fighter!'
		render_template(self, 'main.html', {
		'welcome_msg':welcome_msg
		})
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	], debug=True)