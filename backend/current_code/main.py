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


def arm_and_takeoff(vehicle1, aTargetAltitude):
	"""
	Arms vehicle and fly to aTargetAltitude.
	"""

	print "arming motors"
	vehicle1.mode = VehicleMode("GUIDED")
	vehicle1.armed = True

	while not vehicle1.armed:
		print "waiting for arming..."
		time.sleep(1)
	
	print "taking off"
	t1 = time.time() #record time of takeoff command
	vehicle1.simple_takeoff(15)
	
	k = 0 
	while vehicle1.mode.name=="GUIDED":
		
		if k % 500000 == 0:
			print "Altitude:", vehicle1.location.global_relative_frame.alt, "m"

		k = k+1

		if vehicle1.location.global_relative_frame.alt>=10: #check to see if it's at 10m
			print "10m altitude reached"
			break;
	
arm_and_takeoff(vehicle, 10)

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
