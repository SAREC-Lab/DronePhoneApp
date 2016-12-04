# Tilt mode (mode 3)
# inputs: x_gravity, y_gravity, z_gravity
# output: coordinates for drone to fly to

import math

bound_right = -86.240807
bound_left = -86.239092
bound_back = 41.519441
bound_forward = 41.518968

pi = 3.1415926535
lat2m = 111063.93 #degrees latitude to meters conversion
lon2m = 83471.18 #longitude to meters

speed = 20 #maximum speed 
angle_m = pi/4 #maximum angle

alt = 9

def parse_str(str_in):
	elem = str_in.split( )

	x_grav = elem[1]
	y_grav = elem[2]
	z_grav = elem[3]

	return x_grav, y_grav, z_grav

def vector_loc(loc1, dist, angle):
	#return a location which is 'dist' meters away from loc1 (in the direction defined by angle)
	
	if angle>=360:
		angle = angle-360
	if angle < 0:
		angle = angle+360
	
	lat = loc1.lat + dist/lat2m*math.cos(math.radians(angle))
	lon = loc1.lon + dist/lon2m*math.sin(math.radians(angle))

	return lat, lon

def new_coordinates(str_in, loc_c):

	[x_grav, y_grav, z_grav] = parse_str(str_in)

	x_angle = math.atan(math.abs(x_grav/z_grav))
	y_angle = math.atan(math.abs(y_grav/z_grav))

	x_speed = speed *x_angle/angle_m
	y_speed = speed *y_angle/angle_m

	if x_angle > angle_m:
		x_speed = speed
	if y_speed > angle_m:
		y_speed = speed

	head = math.degrees(math.atan(y_angle/x_angle)) +180
	speed_avg = math.sqrt(y_speed*y_speed + x_angle*x_angle)

	[new_lat, new_lon] = vector_loc(loc_c, 10, head)

	if new_lat>bound_back:
		new_lat = bound_back
	elif new_lat<bound_forward:
		new_lat = bound_forward
	elif new_lon>bound_right:
		new_lon = bound_right
	elif new_lon < bound_left
		new_lon = bound_left

	return [new_lat, new_lon, alt, speed_avg]


	








	
