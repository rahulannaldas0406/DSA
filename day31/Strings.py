#Find the first occurrence of a character in a given string.

'''w="rahul"

ch="l"'''
# for i in range(0,len(w)):
#     if w[i]==ch:
#         print(i)
'''count=-1
for i in w:
    count+=1
    if i==ch:
        print(count)'''

#Find the last occurrence of a character in a given string.

'''a="rahul"
ch=""
index=-1
for i in range(0,len(a)):
    if a[i]==ch:
        index=i
    
print(index)'''


'''a="banana"

ch="a"
arr=[0]*len(a)
k=0
for i in range(0,len(a)):
    if a[i]==ch:
        arr[k]=i
        k+=1
    else:
        continue
print(arr)'''

'''a="banana"
ch="a"
count=0
for i in range(0,len(a)):
    if a[i]==ch:
        count+=1
print(count)'''


#Find the highest frequency character in a string.\

a=""
count={}

for i in range(0,len(a)):
    if a[i] in count:
        count[a[i]]+=1
    else:
        count[a[i]]=1
max_char=None
max_count=0

for char,freq in count.items():
    if freq>max_count:
        max_count=freq
        max_char=char
    else:
        pass

print(max_char,max_count,"times repeated")

# student={
#     "name":"rahul",
#     "age":18,
#     "email":"rahulannaldas@gamil.com"

# }

# print(student)
# print("hi")