import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 3030)) # Подключаемся к нашему серверу.



while True:
	print("client2")
	client.send("Client 2 ".encode("utf-8"))
	break
	
	# take_data = client.recv(1024)
	# print(take_data.decode("utf-8"))

	# command = input("Принять? y/n: ")
	# if command == "y":
	# 	print("принято", '\n')
	# 	while True:
	# 		command2 = input("Завершили? y/n: ")
	# 		if command2 == "y":
	# 			break
	# 		else:
	# 			continue


client.close()
	