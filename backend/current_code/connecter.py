from firebase import firebase

class connecter:

	def __init__(self, site):
		self.firebase = firebase.FirebaseApplication(site, None)
		
	def getData(self, direct):
		result = self.firebase.get(direct, None)
		return result