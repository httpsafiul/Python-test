# 1. reverse a string without using built in methods of python

str = 'Hello World'

for i in range(len(str)):
    print("1: ", str[len(str)-i-1])

print("\n")

# 2. create a list and display the odd indexed elements of this list

list1 = ["Safiul", "Subhradeep Da", 12, "Cat", 23, 1, 2, 3, 4, 5, 6]

for i in range(len(list1)) :
    if(i%2 != 0):
        print("2: ", list1[i])

print("\n")

# 3. create a list and prove it is a list

if type(list1) is list:
    print("3: It is a list")
else:
    print("3: It is not a list")


print("\n")


# 4. remove vowels from a string

str2 = "I am having a good time."
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
str3 = ""

for e1 in str2:
    vowel = False
    for e2 in vowels:
        if e1 is e2:
            vowel = True
    if(vowel is False):
        str3 = str3 + e1

            #str3 = str3 + str2[i]
print("4: Original String: " + str2)
print("4: Modified String: " + str3)
 
print("\n")

# 5. remove numbers from alpha-numeric string

alphanum = "abc1243jA123lihaih"

alpha = ''.join([i for i in alphanum if not i.isdigit()])
 
print("5: Original String ", alphanum)
print("5: Modified String ", alpha)