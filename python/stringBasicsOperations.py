
#The len() function used for strings returns a number of characters
word = "Kiran"
print(len(word))  #output: 5

empty_string = ""
print(len(empty_string))  #output: 0

backSlash_string = "I\'m"
print(len(backSlash_string))  #output: 3

#Operations on strings
#1. concatenated(join) - performed by the + operator (note: it's not an addition) 
#2. replicated - second by the * operator (note again: it's not a multiplication)

String1 = "Kiran"
String2 = "Kumar"
String3 = String1 + " " + String2
print(String3)  #output: Kiran Kumar

String4 = String1 * 3
print(String4)  #output: KiranKiranKiran

#you can put the number before the string, or vice versa, 
# the result will be the same - a new string created by the nth replication of the argument's string.
String5 = 2 * String1
print(String5)  #output: KumarKumar


#ord() - To know a specific character's ASCII/UNICODE code point value.
char_1 = 'a'
char_2 = ' ' #space
print(ord(char_1)) #ouput - 97
print(ord(char_2)) #output - 3

#char() - To know the code point (number) and want to get the corresponding character.
print(chr(97)) #output - a
print(chr(945)) #output - α

#Slicies - To get a substring from a string, we can use slicing. The syntax is string[start:end:step].
name = "Kiran Kumar"
print(name[0:5])  #output: Kiran #Every character from index 0 to 5
print(name[6:11]) #output: Kumar #Every character from index 6 to 11
print(name[1:3])  #output: ir #Every character from index 1 to 3
print(name[3:11]) #output: an Kumar #Every character from index 3 to 11
print(name[:3])   #output: Kir #Every character from the beginning to index 3
print(name[3:8])  #output: an K #Every character from index 3 to 8
print(name[8:11]) #output: umar # Every third character
print(name[::2])  #output: KrnKmr # Every second character
print(name[1::2]) #output: ira uar # Every second character starting from index 1

#The in and not in operators
#in - it simply checks if its left argument (a string) can be found anywhere within the right argument (another string).
#not in - it checks if its left argument (a string) cannot be found anywhere within the right argument (another string).
print("Kiran" in name)  #output: True
print("kiran" in name)  #output: False
print("Kumar" not in name)  #output: False

#min() - To find the minimum element of the sequence
print((min("kiranKumar"))) #output: K #The minimum element is the one with the lowest ASCII value, which is K in this case.
print((min("abcdAbcde"))) #output:  A #The minimum element is the one with the lowest ASCII value, which is A in this case.

#max() - To find the maximum element of the sequence
print((max("kiranKumar"))) #output: r #The maximum element is the one with the highest ASCII value, which is r in this case.
print((max("abcdAbcde"))) #output: e #The maximum element is the one with the highest ASCII value, which is e in this case.
print((max("abcdefghzABCDEFGHZ"))) #output: z #The maximum element is the one with the highest ASCII value, which is z in this case.

#index() - To find the index of a specific character in a string
print(name.index('K'))  #output: 0 #The index of the first occurrence of 'K' is 0
print(name.index('m'))  #output: 5 #The index of the first occurrence of 'm' is 8

#list() - To convert a string into a list of characters
print(list(name))  #output: ['K', 'i', 'r', 'an', ' ', 'K', 'u', 'm', 'a', 'r'] 

#count() - To count the number of occurrences of a specific character in a string'
print(name.count('a'))  #output: 3 #The character 'a' occurs 3 times in the string