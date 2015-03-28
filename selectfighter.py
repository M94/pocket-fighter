import webapp2
import common

class SelectFighter(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('User id not specified')
	def post(self):
		uid = self.request.get('uid')
		common.render_template(self, 'main.html', {
		'uid': uid
		})
		