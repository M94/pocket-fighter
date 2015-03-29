import webapp2
import common
import database

from google.appengine.ext import ndb
		
class Fight(webapp2.RequestHandler):
	def post(self):
		uid = self.request.get('uid')
		mid = self.request.get('mid')
		match = ndb.Key(urlsafe=mid).get()
		common.render_template(self, 'fight.html', {
		'uid': uid,
		'mid': mid,
		'match': match
		})
		