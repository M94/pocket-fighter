import webapp2
import common

class ProcessFighter(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('You did not specify a fighter name.')
	def post(self):
		fighter_name = self.request.get('fighter_name')
		uid = self.request.get('uid')
		self.response.out.write('Player ' + uid + 'chooses ' + fighter_name)
		