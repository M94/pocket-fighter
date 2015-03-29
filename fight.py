import webapp2
import common
		
class Fight(webapp2.RequestHandler):
	def post(self):
		uid = self.request.get('uid')
		mid = self.request.get('match_id')
		common.render_template(self, 'fight.html', {
		'uid': uid,
		'match_id': mid
		})
		