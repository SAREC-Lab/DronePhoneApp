import pyrebase


class connector:

	def __init__(self, config):
		self.firebase = pyrebase.initialize_app(config)
		self.db = self.firebase.database()
		
	def getData(self, var):
		result = self.db.child(var).get().val()
		return result
