import webapp2

from google.appengine.ext import ndb

class Fighter(ndb.Model):
	name = ndb.StringProperty() 
	max_hp = ndb.IntegerProperty(default=100)
	current_hp = ndb.IntegerProperty(default=100)
	att = ndb.IntegerProperty(default=10) # Attack value
	
class Player(ndb.Model):
	fighter = ndb.StructuredProperty(Fighter)
	# 0 = not ready, 1 = ready/waiting, 2 = in match, 3 = finished
	status = ndb.IntegerProperty(default=0)
	match_key = ndb.KeyProperty(default=None)
	
class Match(ndb.Model):
	player1 = ndb.StructuredProperty(Player)
	player2 = ndb.StructuredProperty(Player)
	# 1 = player 1's turn, 2 = player 2's turn
	turn = ndb.IntegerProperty(default=1) 

	