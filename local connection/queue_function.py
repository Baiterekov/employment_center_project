# add_queue = []
# count = 1
# while True:
# 	print("To add queue enter 1: ")
# 	print("To exit of queue 2: ")
# 	input_comand = input("comand: ")
# 	print(" ")
# 	if input_comand=="1":
# 		add_queue.append(count)
# 		count = count +1
# 		print(add_queue)
# 	elif input_comand == "2":
# 		if len(add_queue)==0:
# 			print("Nobody in the queue!")
# 			print("")
# 		else: 
# 			add_queue.pop()
# 			print(add_queue)
# 			print("")
# 			count = count - 1
# 	else:
# 		break


# add_queue_service_1 = []
# add_queue_service_2 = []
# add_queue_service_3 = []
# add_queue_service_4 = []

# queue_1 = 100
# queue_2 = 200
# queue_3 = 300
# queue_4 = 400

# while True:
# 	print("service 1: ")
# 	print("service 2: ")
# 	print("service 3: ")
# 	print("service 4: ")
# 	print("To exit of queue 2: ")
# 	input_comand = input("comand: ")
# 	print(" ")
# 	if input_comand=="1":
# 		add_queue.append(count)
# 		count = count +1
# 		print(add_queue)
# 	elif input_comand == "2":
# 		if len(add_queue)==0:
# 			print("Nobody in the queue!")
# 			print("")
# 		else: 
# 			add_queue.pop()
# 			print(add_queue)
# 			print("")
# 			count = count - 1
# 	else:
# 		break


queue_arr = []

queue_1 = 1000
queue_2 = 2000
queue_3 = 3000
queue_4 = 4000

while True:
	print("Service 1 \nService 2\nService 3\nService 4")
	print("чтобы выйти из очередя нажмите 5\n")
	input_command = input("comand: ")
	print("")
	if input_command == "1":
		queue_1 = queue_1 + 1
		queue_arr.append(queue_1)
	elif input_command =="2":
		queue_2 = queue_2 + 1
		queue_arr.append(queue_2)
	elif input_command =="3":
		queue_3 = queue_3 + 1
		queue_arr.append(queue_3)
	elif input_command =="4":
		queue_4 = queue_4 + 1
		queue_arr.append(queue_4)
	elif input_command == "5":
		if len(queue_arr)==0:
			print("В очереди никого")
		else :
			queue_arr.pop(0)
			if len(queue_arr)==0:
				print("В очереди никого")
	else:
		break
	print("Очередь : ", queue_arr)
	print("")


