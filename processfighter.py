import webapp2
import common

class ProcessFighter(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('You did not specify a fighter name.')
	def post(self):
		fighername = self.request.get('fightername')
		self.response.out.write(fightername)
		