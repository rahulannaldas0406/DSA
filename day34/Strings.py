#Find the first occurrence of a word in a given string.

'''def first_occurrence(text, pattern):
    n = len(text)
    m = len(pattern)

    # Loop through the text, but only till valid index
    for i in range(n - m + 1):
        j = 0
        # Check each character of pattern
        while j < m and text[i + j] == pattern[j]:
            j += 1

        # If full pattern matched
        if j == m:
            return i   # return first occurrence index
    
    return -1  # not found


# Example
text = "make my trip"
pattern = "my"

index = first_occurrence(text, pattern)
if index != -1:
    print("First occurrence at index:", index)
else:
    print("Word not found")'''


#Find the last occurrence of a word in a given string.

'''text="you means"
pattern="means"

n=len(text)
m=len(pattern)

for i in range(len(text)-1,-1,-1):
    j=-1
    c=0
    while c<m and text[i-c]==pattern[j]:
        c+=1
        j-=1
    
    if c==m:
        print(i)
        break'''

def last_occurrence(text, pattern):
    n = len(text)
    m = len(pattern)
    last_index = -1   # initially not found

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            last_index = i   # update whenever a match is found
    
    return last_index


# Example
text = "you means i i means you"
pattern = "you"

index = last_occurrence(text, pattern)
if index != -1:
    print("Last occurrence at index:", index)
else:
    print("Word not found")

#Search all occurrences of a word in a given string.

'''text = "ababcabcabababd"
pattern = "abab"

n = len(text)
m = len(pattern)

occurrences = []

for i in range(n - m + 1):       # slide pattern over text
    j = 0
    while j < m and text[i + j] == pattern[j]:
        j += 1
    if j == m:                   # full pattern matched
        occurrences.append(i)

print("Occurrences:", occurrences)   # [0, 8]'''




