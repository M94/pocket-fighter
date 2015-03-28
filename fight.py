import webapp2
import common
	
		
class Fight(webapp2.RequestHandler):
	def post(self):
		uid = self.request.get('uid')
		common.render_template(self, 'fight.html', {
		'uid': uid
		})
		