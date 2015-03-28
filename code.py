import webapp2

import common
import processfighter
import selectfighter
#import waitmatch
#import findmatch
#import fight
#import processfight

class Main:
	def __init__(self):
		self.uid = 0

main = Main()
		
class MainPage(webapp2.RequestHandler):
	def get(self): 
		main.uid = (main.uid + 1) % 2
		welcome_msg = 'Welcome to Pocket Fighter!'
		common.render_template(self, 'main.html', {
		'welcome_msg': welcome_msg,
		'uid': main.uid
		})
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/selectfighter', selectfighter.SelectFighter), # Handles the fighter select screen
	('/processfighter', processfighter.ProcessFighter), # Handles the process for creating a fighter
	#('/waitmatch', waitmatch.WaitMatch), # Handles the match waiting screen
	#('/findmatch', findmatch.FindMatch), # Handles the process of finding a match
	#('/fight', fight.Fight), # Handles the battle screen
	#('/processfight', processfight.ProcessFight), # Handles all the updates for a battle
	], debug=True)