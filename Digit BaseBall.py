import Core

Core.initialPrint()
while 1 :
	n = input("\nhow many digits? : ")

	key = Core.keyGen(n)
	lst = Core.listGen(n)

	while 1 :
		print("                          Your Turn. Ask me.")
		ask = int(input("                          "))
		result = Core.compare(n,key,ask)
		print("                          "+str(result[0])+" Ball "+str(result[1])+" Strike")
	
		if result[0] == str(n) :
			print("You Win!")
			break
	
		print("This is my Turn.")
		myask = Core.keyGenInList(lst)
		print(myask)
		result = input().split(",")
	
		if result[1] == str(n):
			print("I Win!")
			print(key)
			break
	
		lst = Core.listFilt(n,lst,myask,result[0],result[1])
	print("\nonce again!")