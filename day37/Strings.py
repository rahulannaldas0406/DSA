#Find the length of a string.

'''a="abababcdaabdca"
count=0
for i in a:
    count+=1
print("length of string is:",count)'''

#print(len(a))

#Copy one string to another string.

'''a="rahul"
dupl_str=""
for i in a:
    dupl_str+=i
print(dupl_str)'''

#Concatenate two strings.

'''a="Rahul"
b="Annaldas"

print(a+" "+b)'''

'''a="rahul"
b="rahul"'''

'''if a==b:
    print("both are same")
else:
    print("both are not same")'''

'''check=False

for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            check=True
            break
        else:
            check=False
if check==True:
    print("both are equal")
else:
    print("both are not equal")'''

#Convert lowercase string to uppercase.

'''a="xyz"
result=""
for i in a:
    for j in range(0,26):
        if chr(97+j)==i:
            result+=chr(65+j)
print(result)'''


#print(ord('a'))

#Convert uppercase string to lowercase.

'''a="XYZ"

result=""

for i in a:
    for j in range(0,26):
        if chr(65+j)==i:
            result+=chr(97+j)

print(result)'''

a=input("enter you string")

result=""



for i in a:
    if 'a'<=i<='z':
        for j in range(0,26):
            if chr(97+j)==i:
                result+=chr(65+j)
    elif 'A'<=i<='Z':
        for j in range(0,26):
            if chr(65+j)==i:
                result+=chr(97+j)
    else:
        result+=i
print(result)