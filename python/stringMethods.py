#String Methods

#1. Capitalize() method -  First character of the string is converted to uppercase and all other characters are converted to lowercase.
# Not original string is changed, a new string is returned. i.e still name is in lowercase (kiran kumar) but the output is Kiran kumar.
name = "kiran kumar"
print(name.capitalize())  # Output: Kiran kumar
print(' Alpha'.capitalize()) # Output:  alpha - the first character is an element with an index equal to 0, not just the first visible character, here its empty space, so the output is alpha with a space in front of it. 

#2. center() method - Returns a new string of a specified length with the original string centered and padded with spaces on both sides. 
# If the specified length is less than or equal to the length of the original string, the original string is returned.
# The centering is actually done by adding some spaces before and after the string.
name = "kiran kumar"
print(name.center(20))  # Output: '    kiran kumar     ' -  


#3. endswith() method - Returns True if the string ends with the specified suffix, otherwise returns False.
name = "kiran kumar"
print(name.endswith("kumar"))  # Output: True

subject = "Maths"   
print(subject.endswith("s"))  # Output: True
print(subject.endswith("S"))  # Output: False - case sensitive
print(subject.endswith("a"))  # Output: False

#4. find() method - Returns the lowest index of the substring if it is found in the string. If it is not found, it returns -1.
name = "kiran kumar"
print(name.find("kumar"))  # Output: 6 - the index of the first character of the substring "kumar" in the string "kiran kumar" is 6
print(name.find("Kumar"))  # Output: -1 - case sensitive, "Kumar" is not found in "kiran kumar"
print(name.find("a"))  # Output: 4 - the index of the first occurrence of "a" in "kiran kumar" is 4
print(name.find("z"))  # Output: -1 - "z" is not found in "kiran kumar"

#5. isalnum() method - Returns True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, otherwise returns False.
name = "kiran123"
print(name.isalnum())  # Output: True - all characters are alphanumeric

name = "Rahul"
print(name.isalnum())  # Output: True - all characters are alphabetic

name  = "123456789"
print(name.isalnum())  # Output: True - all characters are numeric

name = "@#$%^&*()"
print(name.isalnum())  # Output: False - all characters are special characters, not alphanumeric

#6. isalpha() method - Returns True if all characters in the string are alphabetic and there is at least one character, otherwise returns False.
name = "kiran"
print(name.isalpha())  # Output: True - all characters are alphabetic

name = "kiran123"
print(name.isalpha())  # Output: False - contains numeric characters    

name = ""
print(name.isalpha())  # Output: False - empty string, no characters to check


#6. isdigit() method - Returns True if all characters in the string are digits and there is at least one character, otherwise returns False.
number = "1234567890"
print(number.isdigit())  # Output: True - all characters are digits

number = "1234abc"
print(number.isdigit())  # Output: False - contains alphabetic characters

#7. islower() method - Returns True if all characters in the string are lowercase and there is at least one character, otherwise returns False.
name = "kiran"
print(name.islower())  # Output: True - all characters are lowercase

name = "Kiran"
print(name.islower())  # Output: False - contains uppercase character

#8. isspace() method - Returns True if all characters in the string are whitespace and there is at least one character, otherwise returns False.
space_string = "   "
print(space_string.isspace())  # Output: True - all characters are whitespace

space_string = "  a  "
print(space_string.isspace())  # Output: False - contains non-whitespace characters

#9. isupper() method - Returns True if all characters in the string are uppercase and there is at least one character, otherwise returns False.
name = "KIRAN"
print(name.isupper())  # Output: True - all characters are uppercase

name = "Kiran"
print(name.isupper())  # Output: False - contains lowercase character

#10. join() method - Returns a string that is the concatenation of the strings in the iterable (e.g., list, tuple) separated by the string on which the method is called.
words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World - joins the words in the list 

words = ["Python", "is", "fun"]
print("-".join(words))  # Output: Python-is-fun - joins the words in the list with a hyphen as separator

#11. lower() method - Returns a new string with all characters converted to lowercase.
name = "KIRAN KUMAR"
print(name.lower())  # Output: kiran kumar - all characters are converted to lowercase

#12. lstrip() method - Returns a new string with leading whitespace removed. If a string is passed as an argument, it removes all leading characters that are present in that string.
name = "   kiran kumar"
print(name.lstrip())  # Output: kiran kumar - leading whitespace is removed

name = "www.google.com"
print(name.lstrip("www."))  # Output: google.com - leading "www." is removed

#13. replace() method - Returns a new string with all occurrences of a specified substring replaced with another substring.
name = "kiran kumar"
print(name.replace("kumar", "nagaraja"))  # Output: kiran nagaraja

#14. rfind() method - Returns the highest index of the substring if it is found in the string. If it is not found, it returns -1.
name = "kiran kumar"
print(name.rfind("kumar"))  # Output: 6 - the index of the last occurrence of "kumar" in "kiran kumar" is 6

print("tau tau tau".rfind("ta")) # Output: 8 - the index of the last occurrence of "ta" in "tau tau tau" is 8

#15. rstrip() method - Returns a new string with trailing whitespace removed. If a string is passed as an argument, it removes all trailing characters that are present in that string.
name = "kiran kumar   "
print(name.rstrip())  # Output: kiran kumar - trailing whitespace is removed    

#16. split() method - Returns a list of substrings by splitting the original string at each occurrence of the specified separator. If no separator is specified, it splits at whitespace.
name = "kirakumar"      
print(name.split())  # Output: ['kirakumar'] - splits at whitespace

name = "kiran kumar b n"
print(name.split(" "))  # Output: ['kiran', 'kumar', 'b', 'n'] - splits at space character


#17. startswith() method - Returns True if the string starts with the specified prefix, otherwise returns False.
name = "kiran kumar"
print(name.startswith("kiran"))  # Output: True - the string starts with "kiran"
print(name.startswith("Kiran"))  # Output: False - case sensitive, the string does not start with "Kiran"

#18. strip() method - Returns a new string with leading and trailing whitespace removed. If a string is passed as an argument, it removes all leading and trailing characters that are present in that string.
name = "   kiran kumar   "
print(name.strip())  # Output: kiran kumar - leading and trailing whitespace is removed

#19. swapcase() method - Returns a new string with uppercase characters converted to lowercase and vice versa.
name = "Kiran Kumar"
print(name.swapcase())  # Output: kIRAN kUMAR - uppercase characters are converted to lowercase and vice versa

name = "ABCDEFGH"
print(name.swapcase())  # Output: abcdefgh - all uppercase characters are converted to lowercase

name = "abcdefgh"
print(name.swapcase())  # Output: ABCDEFGH - all lowercase characters are converted to uppercase

#20. title() method - Returns a new string with the first character of each word converted to uppercase and all other characters converted to lowercase.
name = "kiran kumar"
print(name.title())  # Output: Kiran Kumar - first character of each word is converted to uppercase and all other characters are converted to lowercase

name = "I know that I know nothing. Part 1"     
print(name.title())  # Output: I Know That I Know Nothing. Part 1 - first character of each word is converted to uppercase and all other characters are converted to lowercase

#21. upper() method - Returns a new string with all characters converted to uppercase.
name = "kiran kumar"
print(name.upper())  # Output: KIRAN KUMAR - all characters are converted to uppercase
