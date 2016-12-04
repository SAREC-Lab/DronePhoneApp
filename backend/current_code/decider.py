import talker
import mode2
import mode3

class decider:

	def __init__(self):
		self.mode = None
		
	def sendCommand(self, data, vehicle):
		currentTalker = talker.talker()
		data = self.interpretInputData(data)
		#if data['mode'] != self.mode:
		#	self.changeMode(self, data['mode'])
		if data == 'LAND' or data == 'TAKEOFF':
			currentTalker.sendDroneCommand(data, vehicle)
		else:
			command = mode3.new_coordinates(data, vehicle.location.global_relative_frame)
			currentTalker.sendDroneCommand(command, vehicle)
	
	def changeMode(self, mode):
		self.mode = mode
		
	def interpretInputData(self, data):
		return data
