#date: 12/14/2020
#time: 7:26 PM

import sys	#in this program this is to use the exit command for quitting the program when I want to

word = 'Dance Plus is my most favor@ite game'
dance = list()	#this will initate an empty list
dance.append('Dance')	#this will update the list with the parameter
dance.append('hello')
dance.append(99)
print('printing the updated dance list', dance)

words = word.split()	#this will split the sentence on every space from default. We can specify the delimeter operator by specifying it as parameter.

print('printing the spitted string as a list', words )
pieces = words[5].split('@')

print('printing a further splitted list of word favorite', pieces)
