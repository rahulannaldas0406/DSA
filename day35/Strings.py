#Count occurrences of a word in a given string.


#overlapping 


'''text = "ababcabcabababd"
pattern = "abab"

n = len(text)
m = len(pattern)

count=0

for i in range(n - m + 1):       # slide pattern over text
    j = 0
    while j < m and text[i + j] == pattern[j]:
        j += 1
    if j == m:                   # full pattern matched
        count+=1

print("count of occurance",count)   '''

#non-overlapping 

'''text = "ababcabcabababd"
pattern = "abab"

n = len(text)
m = len(pattern)

count=0
i=0
while i<=n-m:
    j=0
    while j<m and text[i+j]==pattern[j]:
        j+=1
    if j==m:
        count+=1
        i+=m
    else:
        i+=1
print(count)'''

#A Trim leading white space characters from a given string.

'''a="  hello world  "

start=0
while start< len(a) and a[start]==" ":
    start+=1
end=len(a)-1
while end>=0 and a[end]== " ":
    end-=1

result=""
for i in range(start,end+1):
    result+=a[i]
print(result)'''

