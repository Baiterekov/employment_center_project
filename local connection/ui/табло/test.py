text1 = ""
text2 = ""
text3 = ""
text4 = ""

arr_text = []

count = 0
while True:
	input_command = input("command: ")

	if input_command == "9":
		break
	else:
		count = count + 1
		arr_text.append(count)
	try:
		text1 = arr_text[0]
		text2 = arr_text[1]
		text3 = arr_text[2]
		text4 = arr_text[3]
		print(text1)
	except:
		print("SSS")	
	print("GGG")	
	
