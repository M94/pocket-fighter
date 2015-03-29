import webapp2
import common
import database

from google.appengine.ext import ndb
		
class ProcessFight(webapp2.RequestHandler):	
	def post(self): 
		# 0 = invalid param/connection error | 1 = your turn | 2 = opponent's turn 
		uid = self.request.get('uid') # user id
		mid = self.request.get('mid') # match id
		cmd = self.request.get('cmd') # command (optional)
		response = 0
		player_key = ndb.Key(urlsafe=uid)
		match_key = ndb.Key(urlsafe=mid)
		player = ndb.Key(database.Player, player_key.id()).get()
		match = ndb.Key(database.Match, match_key.id()).get()
		if player and match:
			if match.player1 == player and match.turn == 1:
				response = 1
			else: 
				if match.player2 == player and match.turn == 2:
					response = 1
				else:
					response = 2
			if cmd:
				if response == 1:
					# Carry out player's turn
					match.turn = (match.turn % 2) + 1 # Set to other player's turn
					match.put() # Update match
		self.response.out.write(response)
		
		