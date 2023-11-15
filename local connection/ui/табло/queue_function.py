
queue_arr = []
num_queue = []

count = 1

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

		num_queue.append(count)
		count = count+1

	elif input_command =="2":
		queue_2 = queue_2 + 1
		queue_arr.append(queue_2)

		num_queue.append(count)
		count = count+1

	elif input_command =="3":
		queue_3 = queue_3 + 1
		queue_arr.append(queue_3)

		num_queue.append(count)
		count = count+1

	elif input_command =="4":
		queue_4 = queue_4 + 1
		queue_arr.append(queue_4)

		num_queue.append(count)
		count = count+1


	elif input_command == "5":
		if len(queue_arr)==0:
			print("В очереди никого")
		else :
			queue_arr.pop(0)
			num_queue.pop()
			count = count -1
			if len(queue_arr)==0:
				print("В очереди никого")
	else:
		break
	print("Очередь : ", queue_arr)
	print("Номер   : ", num_queue)
	print("")


