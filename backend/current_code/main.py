from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
import math
import random
import master

#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Connects to SITL on local PC by default.')
parser.add_argument('--connect', help="vehicle connection target string.")
args = parser.parse_args()

connection_string = args.connect


# Connect to the Vehicle. 
#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
print "\nConnecting to vehicle on: %s" % connection_string
vehicle = connect(connection_string, wait_ready=True)

print " Is Armable?: %s" % vehicle.is_armable
print " Global Location: %s" % vehicle.location.global_frame


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
		if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.90:
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
	
config = {
  "apiKey": "AIzaSyAwV9FXEvHaDjTr16yOfcoK14d0GrrGfRQ",
  "authDomain": "dronephone-a53c9.firebaseio.com",
  "databaseURL": "https://dronephone-a53c9.firebaseio.com",
  "storageBucket": "dronephone-a53c9.appspot.com"
}
currentMaster = master.master()
currentMaster.activateCallLoop(config, vehicle)

close_shop()
