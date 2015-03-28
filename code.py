import webapp2

import common
#import processfighter
import selectfighter
#import waitmatch
#import findmatch
#import fight
#import processfight

class Main:
	def __init__(self):
		self.uid = 0
		self.waitlist = []

main = Main()
		
class MainPage(webapp2.RequestHandler):
	def get(self): 
		main.uid = (main.uid + 1) % 2
		welcome_msg = 'Welcome to Pocket Fighter!'
		common.render_template(self, 'main.html', {
		'welcome_msg': welcome_msg,
		'uid': main.uid
		})
		
class ProcessFighter(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('You did not specify a fighter name.')
	def post(self):
		fighter_name = self.request.get('fighter_name')
		uid = self.request.get('uid')
		main.waitlist.append(uid)
		self.response.out.write('Player ' + uid + ' chooses ' + fighter_name)
		
class FindMatch(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('User id not specified')
	def post(self):
		uid = self.request.get('uid')
		response = 0 # no match found
		try:
			main.waitlist.index(uid) 
			for other_uid in wait.list:
				if uid != other_uid:
					main.waitlist.pop(uid)
					main.waitlist.pop(other_uid)
					response = 1 # match found
		except:
			response = -1 # error, player not in waitlist
		
		self.out.response.write(response)
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/select_fighter', selectfighter.SelectFighter), # Handles the fighter select screen
	('/process_fighter', ProcessFighter), # Handles the process for creating a fighter
	#('/wait_match', waitmatch.WaitMatch), # Handles the match waiting screen
	('/find_match', FindMatch), # Handles the process of finding a match
	#('/fight', fight.Fight), # Handles the battle screen
	#('/process_fight', processfight.ProcessFight), # Handles all the updates for a battle
	], debug=True)