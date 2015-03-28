import webapp2
import common

class WaitMatch(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('User id not specified')
	def post(self):
		uid = self.request.get('uid')
		common.render_template(self, 'wait_match.html', {
		'uid': uid
		})
		