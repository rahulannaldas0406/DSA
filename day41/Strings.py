#Write a program to convert a sample sentence string into an array of all the words in the sentence.
#  Example: Input->‘Hello World’; Output->[‘Hello’,‘World’]

'''a="Hello world"
result=""
arr=[]*len(a)

for i in range(0,len(a)):
    if a[i]!=" ":
        result+=a[i]
        
        # break
    else:
        arr.append(result)
        result=""
arr.append(result)
print(arr)'''


#proper dsa method

'''a = "Hello world"
arr = []
start = 0

for i in range(len(a)):
    if a[i] == " ":
        arr += [a[start:i]]   # concatenating lists, not using append
        start = i + 1

# Add the last word
arr += [a[start:]]
print(arr)'''




'''n=5


for i in range(1,n+1):
    for k in range(0,n-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#Write a program to eliminate all numeric characters from a string.
#  Example: Input->‘Q1STR5684A’; Output-> ‘QSTRAK’
    
'''a="Q1STR5684A"
num='1234567890'
result=""

for i in a:
    if i not in num:
        result+=i
    
print(result)'''

#Write a program to take a string and print only the numeric characters.
#  Example: Input->‘Q1STR5684AK’; Output->‘15684’

'''a="Q1STR5684A"
num='1234567890'
result=""

for i in a:
    if i in num:
        result+=i
    
print(result)'''

