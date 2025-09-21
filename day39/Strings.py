#Elimination of zeroes from a given number.

'''a="123000103300130500"

result=""

for i in a:
    if i=="0":
        pass
    else:
        result+=i
print(result)'''

#Write a program to take a string and print only the numeric characters using. 
# Example: Input->‘Q1STR5684AK’; Output->‘15684'

a="Q1STR5684AK"
#num="1234567890"
result=""

'''for i in a:
    for j in num:
        if j==i:
            result+=i
print(result)'''

'''for i in a:
    if '0'<=i<='9':
        result+=i
print(result)'''

#Search for a given number in an array

'''a=[20,30,40,55]

n=40

for i in range(0,len(a)):
    if a[i]==n:
        print(i)'''

#Print the number of words in a given string

'''a=" i never fall in love"
count=0
in_word=False
for i in a:
    if i!=" ":
        if not in_word:
            count+=1
            in_word=True
    else:
        in_word=False
print("total number of words in give sentence:",count)'''


'''result=""

arr=[]


for i in range(0,len(a)):
    if a[i]!=" ":
        result+=a[i]
    else:
        arr.append(result)
        result=""'''

'''for i in range(0,len(a)):
    if a[i]==" ":
        count+=1
    
print("total number of words in give sentence:",count)'''



#Remove the single spaces from a given sentence

a="i love you    soo much"

'''sp_count=0
result=""
for i in a:
    if i!=' ':
        result+=i
    elif sp_count>1:
        result+=i
        sp_count=0
    else:
        sp_count+=1
    
print(result)'''

'''result=""
count=0
i=0
while i<len(a):
    if a[i]!=' ':
        result+=a[i]
        i+=1
    else: 
        count+=1
        if count==1:
            continue
        else:
            result+=a[i]
            i+=1
            
    
print(result)'''
in_word=False

if not in_word:
    in_word=True
print(in_word)
# result=""
# for i in a:
#     if i!=" ":
#         result+=i
# print(result)

'''for i in a:
    if i==" ":'''
