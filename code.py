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
		
class ProcessFighter(webapp2.RequestHandler)
	def post(self):
		fighter_name = self.request.get('fighter_name')
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	('selectfighter', SelectFighter), # Handles the fighter select screen
	('processfighter', ProcessFighter), # Handles the process for creating a fighter
	('waitmatch', WaitMatch), # Handles the match waiting screen
	('findmatch', FindMatch), # Handles the process of finding a match
	('fight', Fight), # Handles the battle screen
	('processfight', ProcessFight), # Handles all the updates for a battle
	], debug=True)