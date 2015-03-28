import webapp2
import common
import move 

class Fighter:

	def __init__(self, name, hp, att, move1):
		self.name = name 
		self.maxhp = hp
		self.current_hp = hp
		self.att = att
		self.move1 = Move('Tackle', 5)
		self.alive = true
		
	def take_damage(self, dmg) {
		self.current_hp -= dmg
	}	
	
	def update(self) {
		if(self.current_hp < 0) {
		self.alive = false
		}
		#update character
	}