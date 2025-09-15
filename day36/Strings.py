#Trim trailing white space characters from a given string.

'''a="hello world   "

n=len(a)

lastindex=-1
result=""
for i in range(n-1,-1,-1):
    if a[i]==" ":
        lastindex=i
        break
for i in range(0,lastindex+1):
    result+=a[i]
print(result)'''

#Trim both leading and trailing white space characters from a given string.

'''a="  hello world  "

start_index=-1

result=""

for i in range(0,len(a)):
    if a[i]!=" ":
        start_index=i
        break
last_index=-1

for i in range(len(a)-1,-1,-1):
    if a[i]!=" ":
        last_index=i
        break
for i in range(start_index,last_index+1):
    result+=a[i]
print(result)'''


# for i in range(5,-1,-1):
#     print(i)

#A String is Palindrome or Not

'''a="madam"
rev=""

for i in range(len(a)-1,-1,-1):
    rev+=a[i]

if rev==a:
    print("it is palindrome")
else:
    print("not palindrome")'''

#A String Is an Anagram or Not

a="listen"
b="sileni"
angaram=False
if len(a)==len(b):
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i]==b[j]:
                angaram=True
                break
            else:
                angaram=False
else:
    print("the both string length not equal so the not angaram string")

if angaram==True:
    print("string  is angaram")
                