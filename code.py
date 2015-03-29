import webapp2
import common
import fight
import processfight
import fighter
import time
import database

from google.appengine.ext import ndb
		
class MainPage(webapp2.RequestHandler):
	def get(self): 
		#n_players = len(database.Player.query().fetch())
		welcome_msg = 'Welcome to Pocket Fighter!'
		common.render_template(self, 'main.html', {
		'welcome_msg': welcome_msg,
		})
		
class SelectFighter(webapp2.RequestHandler):
	def get(self):
		player = database.Player()
		uid = player.put().urlsafe()
		common.render_template(self, 'select_fighter.html', {
		'uid': uid,
		})
			
# Create a fighter from the fighter name supplied
class ProcessFighter(webapp2.RequestHandler):
	def post(self): # Params: uid, fighter_name
		fighter_name = self.request.get('fighter_name')
		uid = self.request.get('uid')
		fi = database.Fighter(name=fighter_name)
		player = ndb.Key(urlsafe=uid).get()
		player.fighter = fi
		player.status = 1
		uid = player.put().urlsafe()
		common.render_template(self, 'process_fighter.html', {
		'uid': uid,
		'fighter_name': player.fighter.name
		})
		
class WaitMatch(webapp2.RequestHandler):
	def post(self):
		uid = self.request.get('uid')
		common.render_template(self, 'wait_match.html', {
		'uid': uid
		})
		
# This handles matchmaking for ready players
class FindMatch(webapp2.RequestHandler):
	def post(self):
		response = 0 # no match found
		uid = self.request.get('uid')
		player_key = ndb.Key(urlsafe=uid)
		player = ndb.Key(database.Player, player_key.id()).get()
		if player.match_key != None: # Opponent has found player
			response = player.match_key.urlsafe()
			player.key.delete() # Remove self from waiting list
		else: # Find opponent in waiting list
			players = database.Player.query().fetch()
			for other_player in players:
				if player != other_player and other_player.status == 1:
					# Found a suitable opponent, create a new match
					# Player 1 = host (creator of the match), player 2 = client
					match = database.Match(player1=player, player2=other_player)
					match_key = match.put()
					other_player.match_key = match_key # Add match key to other player to notify him
					other_player.put()
					response = match_key.urlsafe()
					player.key.delete() # Remove self from waiting list
					return self.response.out.write(response)
		self.response.out.write(response)
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/select_fighter', SelectFighter), # Handles the fighter select screen. 
	('/process_fighter', ProcessFighter), # Handles the process for creating a fighter for a player
	('/wait_match', WaitMatch), # Handles the match waiting screen. Adds the current uid to the waiting list.
	('/find_match', FindMatch), # Handles the process of finding a match
	('/fight', fight.Fight), # Handles the battle screen
	('/process_fight', processfight.ProcessFight), # Handles all the updates for a battle
	], debug=True)