import connecter
import decider

class master:

	def __init__(self):
		self.null = None
		
	def activateCallLoop(self, config, vehicle):
		if config == '':
			pass
		else:
			currentConnect = connecter.connector(config)
		currentDecider = decider.decider()
		data = ''
		while(data != 'END'):
			if config == '':
				data = input('Input: ')
			else:
				data = [currentConnect.getData('x'), currentConnect.getData('y')]
			currentDecider.sendCommand(data, vehicle)
			
			
