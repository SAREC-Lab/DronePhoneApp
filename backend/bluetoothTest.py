import time
import bluetooth
import UpdateJSON

def findPhone():
	target_name = "BRANDON"
	target_address = None

	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		if target_name == bluetooth.lookup_name( bdaddr ):
			target_address = bdaddr
			break

	if target_address is not None:
		print("found target bluetooth device with address "+target_address)
	else:
		print("could not find target bluetooth device nearby")
	return target_address

def serverRecieveData():

	UpdateJSON.updateMapCoordinateData('null', 48.846185, 2.346708)
	UpdateJSON.generateNewFile("currentPositions")
	
	server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	
	port = 2
	server_sock.bind(("",port))
	server_sock.listen(2)
	client_sock,address = server_sock.accept()
	
	print("Accepted connection from "+str(address))
	cont = ''
	while(cont!='END'):
		data = client_sock.recv(1024)
		cont = str(data.decode("utf-8"))
		print("got: "+cont)
		
		micro = cont.split(',')
		if cont != 'END':
			if cont == 'PointA':
				UpdateJSON.updateMapCoordinateData('null', 48.846185, 2.346708)
			elif cont == 'PointB':
				UpdateJSON.updateMapCoordinateData('null', 48.858093, 2.296604)
			elif cont == 'PointC':
				UpdateJSON.updateMapCoordinateData('null', 48.864446, 2.325283)
			UpdateJSON.generateNewFile("currentPositions")
				
	client_sock.close()
	server_sock.close()

def sendData():
	bd_addr = "68:AE:20:21:47:F1"

	port = 1
	
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, port))
	sock.close()
	
	sock.send("hello!!")

	sock.close()
	
def sendRecieve():
	
	server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	
	port = 2
	server_sock.bind(("",port))
	server_sock.listen(2)
	client_sock,address = server_sock.accept()
	
	bd_addr = "68:AE:20:21:47:F1"

	friendPort = 3
	
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, friendPort))
	sock.close()
	
	sock.send("hello!!")
	
	print("Accepted connection from "+str(address))
	cont = ''
	while(cont!='END'):
		data = client_sock.recv(1024)
		print("got: "+str(data.decode("utf-8")))
		cont = input()
	
	
	sock.close()
	client_sock.close()
	server_sock.close()
	
	
#findPhone()
serverRecieveData()
#sendData()