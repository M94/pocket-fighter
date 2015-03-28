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
	('/select_fighter', selectfighter.SelectFighter), # Handles the fighter select screen
	('/process_fighter', processfighter.ProcessFighter), # Handles the process for creating a fighter
	#('/wait_match', waitmatch.WaitMatch), # Handles the match waiting screen
	#('/find_match', findmatch.FindMatch), # Handles the process of finding a match
	#('/fight', fight.Fight), # Handles the battle screen
	#('/process_fight', processfight.ProcessFight), # Handles all the updates for a battle
	], debug=True)