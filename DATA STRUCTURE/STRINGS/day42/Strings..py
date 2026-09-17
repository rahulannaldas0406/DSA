#Write a program to take a string and print the number of characters in the string. 
# Example: Input->‘Hello’; Output->5

'''a="he llo"
count=0

for i in a:
    if i==" ":
        pass
    else:
        count+=1
print(count)'''

#Write a program to take a 16-digit credit card number and replace the first 12 characters with ‘X’. 
# Example:Input->‘9765143265387960’; Output->‘XXXXXXXXXXXX7960’
#num="9765143265387960"
'''count=0
for i in num:
    count+=1
    if count<=12:
        print("*",end="")
    else:
        print(i,end="")'''

#another method is 

'''if len(num)==16:
    result="X"*12+num[12:]
    print(result)
else:
    print("invalid number please try again with different number!")'''
    
#Write a program to take a string and replace all vowels with ‘8’.
#  Example: Input->‘This is awesome’; Output->‘Th8s 8s 8w8s8m8’

'''a="awesome"
vow="aeiouAEIOU"

for i in a:
    if i in vow:
        print("8",end="")
    else:
        print(i,end="")'''

#Write a program to hide the middle six digits of a phone number.
#  Example: Input-> '9876543210'; Output-> '98XXXXXX10'

num="9876543210"

