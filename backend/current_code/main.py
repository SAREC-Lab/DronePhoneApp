from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
import math
import random
import master

#Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect', help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None


#Start SITL if no connection string specified
if not connection_string:
	import dronekit_sitl
	sitl = dronekit_sitl.start_default()
	connection_string = sitl.connection_string()




# Connect to the Vehicle
print( 'Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True)
def arm_and_takeoff(aTargetAltitude):
	"""
	Arms vehicle and fly to aTargetAltitude.
	"""

	print( "Basic pre-arm checks")
	# Don't try to arm until autopilot is ready
	while not vehicle.is_armable:
		print ("Waiting for vehicle to initialise...")
		time.sleep(1)

	print( "Arming motors")
	# Copter should arm in GUIDED mode
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True

	# Confirm vehicle armed before attempting to take off
	while not vehicle.armed:
		print( " Waiting for arming...")
		time.sleep(1)

	print( "Taking off!")
	vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

	#Wait until the vehicle reaches a safe height before processing the goto
	# (after Vehicle.simple_takeoff will execute immediately).
	while True:
		print( " Altitude: ", vehicle.location.global_relative_frame.alt)
		#Break and return from function just below target altitude.
		if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
			print( "Reached target altitude")
			break;
		time.sleep(1)

arm_and_takeoff(10)

vehicle.airspeed = 5
print( "Vehicle speed set to: "+str(vehicle.airspeed))

def close_shop():

	print("Setting LAND mode...")
	vehicle.mode = VehicleMode("LAND")

	print('Close vehicle object')
	vehicle.close()

	if sitl is not None:
		sitl.stop()

	time.sleep(20)
	
	
currentMaster = master.master()
site = ''
direct = ''
currentMaster.activateCallLoop(site, direct, vehicle)

close_shop()
