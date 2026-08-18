#1. Comapre
print(("abc" == "abc"))  # True - Two strings are equal when they consist of the same characters in the same order. By the same fashion
print(("abc" != "ABC"))  # True - two strings are not equal when they don't consist of the same characters in the same order.
print(("abc" < "abd"))  # True - "abc" is less than "abd" because the first character that differs is 'c' which comes before 'd' in the alphabet.
print(("abc" > "abd"))  # False - "abc" is not greater than "abd" because the first character that differs is 'c' which comes before 'd' in

#2. Sort
# Sorting a list of strings in ascending order
names = ["kiran", "rahul", "anil", "suresh"]
names.sort()
print(names)  # Output: ['anil', 'kiran', 'rahul', 'suresh'] - The list of strings is sorted in ascending order based on the Unicode values

# Sorting a list of strings in descending order
names = ["kiran", "rahul", "anil", "suresh"]
names.sort(reverse=True)
print(names)  # Output: ['suresh', 'rahul', 'kiran', 'anil'] - The list of strings is sorted in descending order based on the Unicode values

# Strings vs. numbers
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)   # Output: '13 1.3' - The integer and float are converted to strings and concatenated with a space in between
