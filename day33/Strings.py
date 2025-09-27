#Replace the first occurrence of a character with another in a string

'''a="rjhul"

remove="j"
add_char="a"
b=False
result=""
for i in a:
    if i==remove and not  b:
        b=True
        result+=add_char
    else:
        result+=i
print(result)'''


'''a = "rjhuul"
remove = "u"
add_char = "a"

result = a.replace(remove, add_char, -1)
print(result)  # rahul'''

#Put all occurrences of a character with another in a string.

'''a="banana"

result=""

replaced="x"
char="a"
for i in a:
    if i==char:
        result+=replaced
    else:
        result+=i
print(result)'''



#Find the first occurrence of a word in a given string.

word="make me trip"

find=False

wrd="my"

j=0
x=len(wrd)-1
for i in range(0,len(word)):
    if j==x:
        j=0
    if word[i]==wrd[j]:
        print(i)
        j+=1
    else:
        pass
