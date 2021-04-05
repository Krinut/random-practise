#date: 12/14/2020
#time: 7:56 PM

import sys	#in this program this is to use the exit command for quitting the program when I want to

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']	#creating a list of names
for name in names:
	counts[name] = counts.get(name, 0) + 1	#counting the names in the list and their occurences. get() is a method which checks if the key exists and returns the value is it does. If not, it returns the default value. Therefore, the above line will add the key and set it to 1 if the name is new and will just keep adding the histogram if the name exists.

print(counts)
