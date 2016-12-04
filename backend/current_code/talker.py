from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal

class talker:

	def __init__(self):
		self.null = None
		
	def sendDroneCommand(self, command, vehicle):
		if command == 'LAND':
			vehicle.mode = VehicleMode("LAND")
			while True:
				if vehicle.location.global_relative_frame.alt<=0.5:
					break;
				time.sleep(1)
		elif command == 'TAKEOFF':
			vehicle.simple_takeoff(10)
			while True:
				if vehicle.location.global_relative_frame.alt>=9.5:
					break;
				time.sleep(1)
		else:
			location = LocationGlobalRelative(command[0], command[1], command[2])
			vehicle.simple_goto(location, groundspeed=command[3])


