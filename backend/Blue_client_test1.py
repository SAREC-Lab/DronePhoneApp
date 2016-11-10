import bluetooth

bd_addr = "34:02:86:4D:8E:64"

port = 2
prt_rec = 3

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print 'connected'

while True:
	user_input = raw_input("Some input please: ")
	sock.send(user_input)
	if user_input == "END":
		break

sock.close()
