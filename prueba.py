import socket

# Crear un cliente TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("example.com", 80))
cliente.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
respuesta = cliente.recv(4096)
print(respuesta.decode())
