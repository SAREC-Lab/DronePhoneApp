import talker

class decider:

	def __init__(self):
		self.null = None
		
	def sendCommand(self, data, vehicle):
		currentTalker = talker.talker()
		data = self.interpretInputData(data)
		if data['mode'] != self.mode:
			self.changeMode(self, data['mode'])
		if data['mode'] == 'LAND' or data['mode'] == 'TAKEOFF':
			currentTalker.sendDroneCommand(data['mode'], vehicle)
		else:
			#command = self.mode.translate()
			command = data
			currentTalker.sendDroneCommand(command, vehicle)
	
	def changeMode(self, mode):
		self.mode = mode
		
	def interpretInputData(data):
		return eval('{'+data+'}')