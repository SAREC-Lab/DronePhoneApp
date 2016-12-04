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

speed_scale = 1.5 #maximum speed 
angle_m = pi/4 #maximum angle

alt = 9

def parse_str(str_in):
	elem = str_in.split( )

	x_grav = float(elem[0])
	y_grav = float(elem[1])
	z_grav = float(elem[2])

	return x_grav, y_grav, z_grav

def vector_loc(loc1, x_dist, y_dist):

	
	lat = loc1.lat + x_dist/lat2m
	lon = loc1.lon + y_dist/lon2m

	return lat, lon

def new_coordinates(data_in, loc_c):

	#[x_grav, y_grav, z_grav] = parse_str(str_in)

	x_grav = data_in[0]
	y_grav = data_in[1]

	x_speed = speed_scale *x_grav
	y_speed = speed_scale *y_grav

	speed_avg = math.sqrt(y_speed*y_speed + x_speed*x_speed)

	print x_speed, y_speed, speed_avg

	[new_lat, new_lon] = vector_loc(loc_c, x_speed, y_speed)

	if new_lat>bound_back:
		new_lat = bound_back
	elif new_lat<bound_forward:
		new_lat = bound_forward
	elif new_lon>bound_left:
		new_lon = bound_left
	elif new_lon < bound_right:
		new_lon = bound_right

	print loc_c.lat, loc_c.lon
	print new_lat, new_lon

	return [new_lat, new_lon, alt, speed_avg]


	








	
