#Append the calling code of India(+91) to a given phone number. 
# Example: Input-> '9876543210'; Output-> '+919876543210'

#num=input("enter a mobile number:")

#print("+91",num)

#but they given append should use

'''ind="+91"
for i in num:

    there is no different method using for loop '''

#Check whether a given number is a valid phone number.
#        Example:Input-> '7654893274'; Output-> 'valid'
#        Input-> '785487438754'; Output-> 'invalid'.........(must be 10 digits)
#        Input-> '7854s54839'; Output-> 'invalid'.............(must NOT contain letters)

'''num=input("enter a mobile number)

if len(num)==10:
    print("valid")
else:
    print("invalid")'''


#Check whether a given number is a valid credit card number. Example:
#        Example:
#        Input-> '7463836483647454'; Output-> 'valid'
#        Input-> '74638364836474548'; Output-> 'invalid'...(must be 16 digits)
#        Input-> '7463836w4836o745'; Output-> 'invalid'...(must contain only numbers)

'''num=input("enter a credit card number")

if len(num)==16:
    print("valid")
else:
    print("invalid")'''

#Write a program to add hyphens (-) in between a given credit card number.
#        Example:
#        Input-> '6484638463487486'; Output-> '6484-6384-6348-7486'

'''num=input("enter a credit card number")

count=0

for i in num:
    count+=1
    if count==4:
        print("-",end="")
        count=0
    else:
        print(i,end="")'''

#Sort a given string
#        Example: ‘praveen’=>’aeenprv’

a="rahul"

alp="abcdefghijklmnopqrstuvwxyz"

# for i in a:
#     if i in alp:
#         print(i)

'''for i in range(0,len(alp)):
    for j in range(0,len(a)):
        if alp[i]==a[j]:
            print(alp[i],end="")'''

'''i=0
while i<len(alp):
    j=0
    while j<len(a):
        if alp[i]==a[j]:
            print(a[j],end="")
        j+=1
    i=j
    #i+=1'''
    
#Eliminate Duplicate characters in given string
#        Example: ‘praveengubbala’ => ‘pravengubl’

'''name="praveengubbala"

result=""

for i in name:
    if i not in result:
        result+=i
    
print(result)'''

#Write a program to print only numbers out of a given string
#        Example: let us take pr34s2v9q4
#        The output should be 3,4,2,9,4

'''value="pr34s2v9q4"
num="1234567890"
for i in value:
    if i in num:
        print(i,end=" ")'''
    