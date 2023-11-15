"""
server

import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
server.listen(1) # Начинаем прослушивать входящие соединения.

text_1 = "Оператор принял очередь!"
text_2 = "Оператор свободен!" 

user, address = server.accept()

print ('Connected by',address)
while True:

	data = user.recv(1024)
	print(data.decode("utf-8"))

	comand_1 = input("Принять? y/n: ")
	if comand_1=="y":
		user.send(text_1.encode("utf-8"))
	else:
		break

	while True:
		comand_2 = input("Завершили? y/n: ")

		if comand_2=="y":
			user.send(text_2.encode("utf-8"))
			break
		else:
			continue
		

server.close()

"""

"""
client

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 3030)) # Подключаемся к нашему серверу.

count = 1

text = "Принимай очередь "

send = input("Отправить очередь? y/n: ")

while True:
	text = text + str(count)
	client.send(text.encode("utf-8"))
	take_data = client.recv(1024)
	print(take_data.decode("utf-8"))

	take_data = ""

	take_data = client.recv(1024)
	print(take_data.decode("utf-8"))

	if take_data == "":
		break

	send = input("Отправить новый очередь? y/n: ")		
	count = count+1

	if send =="y":
		continue

client.close()
	
"""