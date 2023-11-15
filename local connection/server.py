import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
server.listen(1) # Начинаем прослушивать входящие соединения.


user, address,  = server.accept()

user2, address2 = server.accept()

queue = 1

service1 = "SERVICE 1"
service1 = "SERVICE 2"
service1 = "SERVICE 3"

print ('Connected by',address)
print ('Connected by',address2)


data = user.recv(1024)
print(data.decode("utf-8"))
data = user.recv(1024)
print(data.decode("utf-8"))

# while True:
# 	print(service1+'\n', service2+'\n', service3+'\n')
# 	enter_service = input("")
# 	if enter_service=="1" or enter_service=="2" or enter_service=="3":
# 		user.send(queue.encode("utf-8"))
# 	else:
# 		break
# 	queue = queue+1
	
# 	# data = user.recv(1024)
		

server.close()
