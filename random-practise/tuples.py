#date: 12/14/2020
#time: 9:46 PM

import sys	#in this program this is to use the exit command for quitting the program when I want to

dance = 'Hello. I am writing this statement to check out a sorting of dictionary statement. This is just a general statement that speaks to you in a way no one can understand. Alright, this is the end of the line and now lets get on to the code'

#this part will make a dictionary with the words and their counts.
counts2 = dict()	#creating an empty dictionary
words = dance.split()	#splitting the sentence into words
for word in words:
	counts2[word] = counts2.get(word, 0) + 1	#for loop to create the histogram loop

#this part will create a list from the dictionary but in value, key format rather than key, value
lst = list()	#creating an empty list
for (k,v) in counts2.items():	#this loop will loop through all the items in the dictionary and then create a list with value, key pair. Here items() returns a list of tuples from the dictionary. also notice that we can iterate two variables in python because of tuples.
	newtup = (v, k)
	lst.append(newtup)

lst = sorted(lst, reverse= True)	#sorted() takes in a seequnce and returns a sorted sequence

for (v,k) in lst:	#this loop will print all the words in the sorted fashion as key, value
	print(k,v)
