<<<<<<< Updated upstream
#Write a program to sort the array based on the number of occurrences of elements 
# Ex: original array: [1,2,5,6,2,1,6,1,2,6,2,1,2]; 
# After the logic: [5,6,6,6,1,1,1,1,2,2,2,2,2]; //5 occurred one time,6 three times,1 occurred 4 times, 2 occurred 5 times

from num2words import num2words

arr=[1,2,3,1,2,3]
count={}
arr1=[]
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
value=[]
for k,v in count.items():
    value.append(v)
sort_value=sorted(value)
print(sort_value)
for i in range(0,len(value)):
    for k,v in count.items():
        if sort_value[i]==v:
            arr1.extend([k]*sort_value[i])
print(arr1)   

/* NOOTE */
/* there is on bug in my code that is If two numbers have the same frequency (say [1,2,3,1,2,3] → all appear twice),
your code may add them in dictionary insertion order (which is fine in Python 3.7+ but not guaranteed before).*/
/*so the acutal code is i asked the chatgpt it give simple but difficult to understand */

arr = [1,2,5,6,2,1,6,1,2,6,2,1,2]

# Sort by frequency, then by value (optional)
arr_sorted = sorted(arr, key=lambda x: (arr.count(x), x))
print(arr_sorted)
# [5, 6, 6, 6, 1, 1, 1, 1, 2, 2, 2, 2, 2]
=======
#Write a program to sort the array based on the number of occurrences of elements 
# Ex: original array: [1,2,5,6,2,1,6,1,2,6,2,1,2]; 
# After the logic: [5,6,6,6,1,1,1,1,2,2,2,2,2]; //5 occurred one time,6 three times,1 occurred 4 times, 2 occurred 5 times

from num2words import num2words

arr=[1,2,3,1,2,3]
count={}
arr1=[]
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
value=[]
for k,v in count.items():
    value.append(v)
sort_value=sorted(value)
print(sort_value)
for i in range(0,len(value)):
    for k,v in count.items():
        if sort_value[i]==v:
            arr1.extend([k]*sort_value[i])
print(arr1)

for i in range(0,len(value)):
    for k,v in count.items():
        if sort_value[i]==v:
            print(k,"occured",num2words(v),"times")

    
>>>>>>> Stashed changes
