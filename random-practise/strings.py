#date: 12/11/2020
#time: 9:22 PM

import sys	#in this program this is to use the exit command for quitting the program when I want to

word = 'Dance Plus'
for letter in word :
	print(letter)

print(word[2:4])	#this thing will print all the letters from (2,4]
print(word[:4])		#this will print from 0-3
print(word[4:])		#this will print from 4-end
print(word[2:20])	#this will print from 2-end. If the second range is not in the limit it will go till the end and then stop.

word2 = 'is my favorite game'
word3 = word + ' ' + word2	#this will conentate the strings. Note: the + sign does  not add any space so it needs to be added explicitly.

print('finding an occurence in word', word.find('ance')) 	#find() searches for the first occurence and returns the position of it.

print('replacing favorite in word2 with most favorite in word2', word2.replace('favorite', 'most favorite'))	#this finds the occrurence and replaces it.

print('stripping the white spaces', '   dance   '.lstrip(), '   dance   '.rstrip(), '   dance   '.strip())	#strips off the white spaces from the sentence. the functions are self explanatory

print('seeing if something starts with something', word3.startswith('Dance'), word3.startswith('Krishna'))	#this will return True or False depending on if word3 starts with what I passed into the parameter.
