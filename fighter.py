import webapp2
import common
import move 

class Fighter:

	def __init__(self, name, hp, att, move1):
		self.name = name 
		self.maxhp = hp
		self.current_hp = hp
		self.att = att
		self.move1 = move.Move('Tackle', 5)
		self.alive = 1
		
	def take_damage(self, dmg):
		self.current_hp -= dmg
	
	def attack(self, f2, move):
		damage = self.att+move.get_damage()
		f2.take_damage(damage)
	
	def is_alive(self):
		return self.alive
	
	def update(self):
		if(self.current_hp < 0): 
			self.alive = false
		#update character