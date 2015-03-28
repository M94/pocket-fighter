import webapp2

import common
import selectfighter
import waitmatch
import fight
import processfight
import time

class Main:
	def __init__(self):
		self.uid = 0
		self.wait_list = []
		
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
		main.wait_list.append(uid)
		self.response.out.write('Player ' + uid + ' chooses ' + fighter_name)
		common.render_template(self, 'wait_match.html', {
		'uid': uid
		})
		
		
class FindMatch(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('User id not specified')
	def post(self):
		uid = self.request.get('uid')
		response = -1 # no match found
		for other_uid in main.wait_list:
			if uid != other_uid:
				response = 0 # match id
				return self.response.out.write(response)
		self.response.out.write(response)
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/select_fighter', selectfighter.SelectFighter), # Handles the fighter select screen
	('/process_fighter', ProcessFighter), # Handles the process for creating a fighter and adding player to waitlist
	('/wait_match', waitmatch.WaitMatch), # Handles the match waiting screen
	('/find_match', FindMatch), # Handles the process of finding a match
	('/fight', fight.Fight), # Handles the battle screen
	('/process_fight', processfight.ProcessFight), # Handles all the updates for a battle
	], debug=True)