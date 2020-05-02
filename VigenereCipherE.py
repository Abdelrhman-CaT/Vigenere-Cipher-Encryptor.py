key=input('Enter Encryption key ---> ')
key=key.lower()
alpha_input=input('Enter Alphabetical Order ---> ')
message=input('Enter the message to Encrypt ---> ')

if len(alpha_input) == 26:
	def Custom():


				alpha=alpha_input
				alpha*=2
				alpha=" "+alpha

		

				table_write=open("VigenereTableCustom.txt" , "w")
				table_append=open("VigenereTableCustom.txt" , "a")
		

	
				table_write.write(alpha[0])
				for i in alpha_input :
					table_append.write(i)
				table_append.write("\n")			

				for i in alpha_input :
					table_append.write(i)
					for q in range(alpha.find(i) , alpha.find(i)+26):
						table_append.write(f"{alpha[q]}")
					table_append.write("\n")


				table=open("VigenereTableCustom.txt" , "r")
		
				return table


	

	

	def Custom_Upper():


				ALPHA=alpha_input.upper()
				ALPHA*=2
				ALPHA=" "+ALPHA



				TABLE_write=open("VigenereTableUpperCustom.txt" , "w")
				TABLE_append=open("VigenereTableUpperCustom.txt" , "a")



				TABLE_write.write(ALPHA[0])
				for i in alpha_input.upper():
					TABLE_append.write(i)
				TABLE_append.write("\n")			

				for i in alpha_input.upper():
					TABLE_append.write(i)
					for q in range(ALPHA.find(i) , ALPHA.find(i)+26):
						TABLE_append.write(f"{ALPHA[q]}")
					TABLE_append.write("\n")


				TABLE=open("VigenereTableUpperCustom.txt" , "r")	
		
				return 	TABLE


else:

	while len(alpha_input) != 26:

		print('Your Alphabetical Order isn\'t complete')
		alpha_input=input('Enter Alphabetical Order "make sure you entered 26 character" ---> ')
		
		if alpha_input == '1':
			def Custom():
				table=open("VigenereTableStandard.txt" , "r")
				return table
			def Custom_Upper():	
				TABLE=open("VigenereTableUpperStandard.txt" , "r")
				return TABLE
			break
			
	if len(alpha_input) == 26 :	


			def Custom():


				alpha=alpha_input
				alpha*=2
				alpha=" "+alpha

		

				table_write=open("VigenereTableCustom.txt" , "w")
				table_append=open("VigenereTableCustom.txt" , "a")
		

	
				table_write.write(alpha[0])
				for i in alpha_input :
					table_append.write(i)
				table_append.write("\n")			

				for i in alpha_input :
					table_append.write(i)
					for q in range(alpha.find(i) , alpha.find(i)+26):
						table_append.write(f"{alpha[q]}")
					table_append.write("\n")


				table=open("VigenereTableCustom.txt" , "r")
		
				return table


	

	

			def Custom_Upper():


				ALPHA=alpha_input.upper()
				ALPHA*=2
				ALPHA=" "+ALPHA



				TABLE_write=open("VigenereTableUpperCustom.txt" , "w")
				TABLE_append=open("VigenereTableUpperCustom.txt" , "a")



				TABLE_write.write(ALPHA[0])
				for i in alpha_input.upper():
					TABLE_append.write(i)
				TABLE_append.write("\n")			

				for i in alpha_input.upper():
					TABLE_append.write(i)
					for q in range(ALPHA.find(i) , ALPHA.find(i)+26):
						TABLE_append.write(f"{ALPHA[q]}")
					TABLE_append.write("\n")


				TABLE=open("VigenereTableUpperCustom.txt" , "r")	
		
				return 	TABLE
				




x=Custom().readlines()
X=Custom_Upper().readlines()


def lineread(line_num):
	return x[line_num]

def LINEREAD(LINE_NUM):
	return X[LINE_NUM]


row0=list(lineread(0))
row0.remove(' ')
row0.remove('\n')

ROW0=list(LINEREAD(0))
ROW0.remove(' ')
ROW0.remove('\n')	



def key_analysis():
	global Y_Axis
	Y_Axis=[]
	length=len(key)
	for i in range(0,length):
		CoorY=lineread(0).find(key[i])		
		Y_Axis.append(CoorY)
	
	return Y_Axis	


def message_analysis():
	message_as=[]
	length=len(message)
	for i in range(0,length):
		if message[i] not in row0:
			if message[i] in ROW0:
				CoorX=LINEREAD(0).find(message[i])
			else:	
				CoorX=message[i]
		else:
			CoorX=lineread(0).find(message[i])
		message_as.append(CoorX)	
	global X_Axis
	X_Axis=[]
	for i in message_as:
		if i not in range(0,30):
			Axis = i
		else:
			Axis=x[i]
		X_Axis.append(Axis)

	return X_Axis



key_analysis()
message_analysis()



if len(X_Axis) > len(Y_Axis):
	diff= len(X_Axis) - len(Y_Axis)
	Y_Axis=Y_Axis * diff * 2

if len(Y_Axis) > len(X_Axis):
	diff= len(Y_Axis) - len(X_Axis)
	for i in range(0,diff):
		Y_Axis.pop()

def Encrypt():
	y_Axis=Y_Axis
	for i in range(0,len(message)):
		if X_Axis[i] not in x :
			y_Axis.insert(i,0)
			y_Axis.pop()
			Cipher=message[i]
		else:
			Cipher=X_Axis[i][y_Axis[i]]
		if message[i].isupper():
			Cipher=Cipher.upper() 	
		print(Cipher,end='')

Encrypt()


	