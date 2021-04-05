#date: 12/09/2020
#time: 9:45 PM

import sys	#in this program this is to use the exit command for quitting the program when I want to

##############################
#if-else-elif condition statements
#defining a function. We use def as the keyword. More details are still to be read in a textbook about the arguments and stuff
def compare(x, y, z):
	if x<y and x<z:
		print("first is smallest")
		return x
	elif y<x and y<z:
		print("second is the smallest", y)
		return y
	else :
		print("Third is smallest", z)
		return z
###############################
for i in [1, 2, 3, 4] :
	choice = 'y'
	while choice != 'n' :
		xstr = input("Enter the first value ")	#Inout through this is in string format. we need to convert it to the desired type conversions
		ystr = input("enter the second value ")
		zstr = input ("enter third value ")

		############
		#try and except is a way to try a line of code that can malfunction without affecting the rest of the code. If the try works it ignores the expect and moves on to the next line. If not, it invokes the expect and moves on to the next line. So adding a system exit if you want to exit is a good idea there.
		try :
			x = int(xstr)
		except :
			print("first is not an integer", xstr)
			sys.exit(0)		#command to exit the program
		try :
			y = int(ystr)
		except :
			print("second is not an integer", ystr)
		try :
			z = int(zstr)
		except :
			print("Third is not an integer", zstr)

		#################################
		print("The result of comparision is:", compare(x, y, z))
		choice = input("Do you want to try again? (y/n): ")
		if choice != 'y' and choice != 'n' :
			print("please enter either y/n from next time. Thank you")
			break	#breaks from the loop
		else :
			continue	#go backs to the first line which means teh current iteration is completed and the next itiation will be run without running the next lines
	print(i)

print("Thank you for your time,\nkrishna")
print(type(x))	#type() returns the class/type of the variable we are using
