from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal

class talker:

	def __init__(self):
		self.null = None
		
	def sendDroneCommand(command, vehicle):
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
			vehicle.airspeed = command.speed
			location = LocationGlobalRelative(command.lat, command.lon, command.alt)
			vehicle.simple_goto(location)