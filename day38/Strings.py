#Find a total number of alphabets, digits or special character in a string.

'''

num="1234567890"

U_ch="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

a="rahul2006@gmail.com"
sp_count=0
dig_count=0
alp_count=0'''

'''for sp in sp_ch:
    for i in a:
        if i==sp:
            sp_count+=1
print("number of special character:",sp_count)
for n in num:
    for i in a:
        if i==n:
            dig_count+=1
print("number of digits:",dig_count)

for u in U_ch:
    for i in a:
        if i==u:
            alp_count+=0
for l in L_ch:
    for i in a:
        if i==l:
            alp_count+=1
print("number of alphabates:",alp_count)'''

# this is another method of the problem


'''for i in a:
    if i in sp_ch:
        sp_count+=1
    elif i in num:
        dig_count+=1
    else:
        alp_count+=1

print("number of special character:",sp_count)
print("number of digits:",dig_count)
print("number of alphabates:",alp_count)'''


#this is python in-built methods use code

'''a = "rahul2006@gmail.com"

alp_count = 0
dig_count = 0
sp_count = 0

for i in a:
    if i.isalpha():       # checks alphabets (A-Z, a-z)
        alp_count += 1
    elif i.isdigit():     # checks digits (0-9)
        dig_count += 1
    else:                 # everything else = special character
        sp_count += 1

print("Number of alphabets:", alp_count)
print("Number of digits:", dig_count)
print("Number of special characters:", sp_count)'''

#Count the total number of vowels and consonants in a string.

'''a="rahul"
vow_count=0
con_count=0
vow_str="aeiou"

for i in a:
    if i in vow_str:
        vow_count+=1
    else:
        con_count+=1
print("number of vowels:",vow_count,number of constant:",con_count)'''

#Count the total number of words in a string.

'''a="i love you rahul"
count=0
for i in a:
    if i!=" ":
        count+=1
    
print(count)'''

#here is different approach


'''a = " i love you rahul "
count = 0
in_word = False

for ch in a:
    if ch != " " and not in_word:  # starting a new word
        count += 1
        in_word = True
    elif ch == " ":
        in_word = False

print("Number of words:", count)'''

#Find the reverse of a string.

'''a="rahul"
result=""
for i in range(len(a)-1,-1,-1):
    result+=a[i]
print(result)'''

#Reverse order of words in a given string.

'''a="i love you rahul"

result=""

for i in range(len(a)-1,-1,-1):
    if a[i]==" ":
        print(result,end=" ")
        result=""

    else:
        result=a[i]+result
print(result)'''

#Reverse of a number using toString, split, reverse and join methods.


a=12345

rev=a.toString().split("").reverse().join("")
print(rev)