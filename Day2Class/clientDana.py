import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 12345))
clientsocket.send('this is a message from dana -- hello dana')