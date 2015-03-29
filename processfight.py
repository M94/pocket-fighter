import webapp2
import common

class Fights:
	def __init__(self):
		self.list = []

class Fight:
	def __init__(self, uid1, uid2):
		self.player1 = uid1
		self.player2 = uid2
		
	def stuff(self, uid):
		if uid == self.player1 or uid == self.player2:
			return 'stuff for ' + uid
		return 'error'
	
fights = Fights()
	
def CreateFight(uid1, uid2):
	fight = Fight(uid1, uid2)
	mid = uid1 + uid2
	fights.insert(mid, fight)
	return mid
		
class ProcessFight(webapp2.RequestHandler):	
	def post(self):
		uid = self.request.get('uid') # user id
		self.response.out.write(fight.stuff(uid))
		
		