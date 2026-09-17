#remove all the spaces from a given string

'''a="hello world"
result=""
for i in a:
    if i!=" ":
        result+=i
    else:
        pass
print(result)'''

'''a="hello world"
i=0
result=""
while i<len(a):
    if a[i]!=" ":
        result+=a[i]
    else:
        pass
    i+=1
print(result)'''

#Search a given string in a sentence(both uppercase and lowercase)

a="hello wrld"

search="world" 

b=False
i=0

while i<len(a):
    j=0
    while j<len(search):
        if search[j]==a[i]:
            b=True
            i+=1
            j+=1
        else:
            break
    i+=1
print(b)
