#Replace the first occurrence of a character with another in a string.
#print(~-6)   # ~0101 = 1010 (two’s complement) → -6
#print(5 << 1)   # 0101 → 1010 = 10
#print(5 << 2)   # 0101 → 10100 = 20

#Find the lowest frequency character in a string.

'''a="banana"
count={}

for i in range(0,len(a)):
    if a[i] in count:
        count[a[i]]+=1
    else:
        count[a[i]]=1
max_char=None
max_count=100

for char,freq in count.items():
    if freq<max_count:
        max_count=freq
        max_char=char
    else:
        pass

print(max_char,max_count,"times repeated")'''

#Count the frequency of each character in a string.

'''a="banana"

count={}

for i in range(0,len(a)):
    if a[i] in count:
        count[a[i]]+=1
    else:
        count[a[i]]=1
print(count)'''

#Remove the first occurrence of a character from a string.

'''a="banana"

char_remove="a"

result=""
removed=False

for i in a:
    if i==char_remove and not removed:
        removed=True
        continue
    result+=i
print(result)'''

#Remove the last occurrence of a character from a string

'''a="banana"
char_remove="a"
result=""
removed=False

for i in range(len(a)-1,-1,-1):
    if a[i]==char_remove and not removed:
        removed=True
        continue
    result+=a[i]
result=result[::-1]
print(result)'''

#Delete all occurrences of a character from a string.

a="banana"
char_remove="a"
result=""
removed=False

for i in a:
    if i==char_remove:
        removed=True
        continue
    result+=i
print(result)