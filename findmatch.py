import webapp2
import common

class Wait:
	def __init__(self):
		self.list = []
		
wait = Wait()

class FindMatch(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('User id not specified')
	def post(self):
		uid = self.request.get('uid')
		response = 0
		try:
			wait.list.index(uid) # Add player if not in list
		except:
			wait.list.append(uid)

		for other_uid in wait.list:
			if uid != other_uid:
				wait.list.pop(uid)
				wait.list.pop(other_uid)
				response = 1
				
		self.out.response.write(response)
		
		
		
		
		