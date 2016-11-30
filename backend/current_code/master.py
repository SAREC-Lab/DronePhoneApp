import connecter
import decider

class master:

	def __init__(self):
		self.null = None
		
	def activateCallLoop(self, site, direct, vehicle):
		if (site == '') and (direct == ''):
			pass
		else:
			currentConnect = connector.connector(site)
		currentDecider = decider.decider()
		data = ''
		while(data != 'END'):
			if (site == '') and (direct == ''):
				print('Input: ')
				data = input()
			else:
				data = currentConnect.getData()
			currentDecider.sendCommand(data, vehicle)
			
			