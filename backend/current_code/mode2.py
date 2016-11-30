# Button mode (mode 2)
# input either 'right', 'left', 'forward', 'backward', 'up', 'down' or 'none', and current location
# output coordinates for drone to fly

bound_right = -86.240807

bound_left = -86.239092

bound_back = 41.519441

bound_forward = 41.518968

alt_low = 5
alt_high = 25

speed = 15

def new_coordinates(direction, loc_c):

	new_lat = loc_c.lat
	new_lon = loc_c.lon
	new_alt = loc_c.alt
	
	if direction == 'left':
		new_lon = bound_left
	elif direction == 'right':
		new_lon = bound_right
	elif direction == 'forward':
		new_lat = bound_forward
	elif direction == 'backward':
		new_lat == bound_back
	elif direction == 'up':
		new_alt = alt_high
	elif direction == 'down':
		new_alt = alt_low
	
	return [new_lat, new_lon, new_alt, speed]

