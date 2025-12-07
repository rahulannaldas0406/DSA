#Strings

'''import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)'''

#reverse a string using without slicing 

'''n="Rahul"
rev=" "
for cha in range(len(n)-1,-1,-1):
    rev=rev+n[cha]
print(rev)'''

#check string is palindrome or not
'''n="madam"#it start on 0 rth index
i=0
j=len(n)-1
while i<j:
    if n[i]!=n[j]:
        print("it is not palindrome")
        break
    i=i+1
    j=j-1
else:
    print("it is palindrome")'''

#Convert all characters in a string to uppercase/lowercase.

'''n="ASSI"
lower=n.lower()
print(lower)

for i in range(1,11):
    for j in range(1,11):
        if i==1 or j==1 or i==10 or j==10:
            print("*",end="")
        else:
            print(end=" ")
    print()'''

#Remove duplicate characters from a string
'''n="naina"
result=""
res=""
for i in n:
    if i not in result:
        result=result+i
    else:
        res=res+i
print(result)
print("dup values",res)'''

#Count frequency of each character
#Input: "hello" → Output: {h:1, e:1, l:2, o:1}'''

n=[1,2,3,4,2,1]
count={}
for i in n:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
for v in count.items():
    print(v)


#Swap case (upper ⇄ lower)
#Input: "PyTHon" → Output: "pYthON"

'''n='pYThon'
str=""
for i in n:
    if i.isupper():
        str=str+i.lower()
    else:
        str=str+i.upper()
print(str)'''

#Check if two strings are anagrams
#Input: "listen", "silent" → Output: True

'''str1="aulrh"
str2="rahul"
count1={}
count2={}
for i in str1:
    if i in count1:
        count1[i]+=1
    else:
        count1[i]=1
for i in str2:
    if i in count2:
        count2[i]+=1
    else:
        count2[i]=1
if count1.items() == count2.items():
    print("TRUE")
else:
    print("FALSE")'''
#we can write in using sort

'''def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # True'''

#Another way to find

'''from collections import Counter

def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

print(are_anagrams("listen", "silent"))  # True'''

'''str="Madam mada:m"
st=str.lower()
sp=":"
new=""
for s in st:
    if s==sp:
        s.remove()
    else:
        new+=s
print(new)
stry=""
strz=""
for i in str:
    stry=stry+i
#print(stry)

for j in range(len(str)-1,-1,-1):
    strz=strz+str[j]
#print(strz)
if stry==strz:
    print("TRUE")
else:
    print("FALSE")'''
