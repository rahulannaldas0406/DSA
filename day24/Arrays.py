#Write a program to remove elements from an array which are not in the ascending order 
# Ex: Original array: [12,34,11,56,37,98,23,67,109,45] Output : [12,34,56,98,109]

# pesudo code

# firstelement=12
# secondelement=34
# thirdelement=secondelelement

'''arr=[12,34,11,56,37,98,23,67,109,45]
li=[arr[0]]
i=0
while i<len(li):
    for j in range(i+1,len(arr)):
        if li[i]<arr[j]:
            li.append(arr[j])
            break
    i+=1
print(li)'''

#Write a program to sort the array based on the number of occurrences of elements 
# Ex: original array: [1,2,5,6,2,1,6,1,2,6,2,1,2]; After the logic: [5,6,6,6,1,1,1,1,2,2,2,2,2]; 
# //5 occurred one time,6 three times,1 occurred 4 times, 2 occurred 5 times


'''arr=[1,2,3,4,2,1,4,2,5,2,1,3,1]

dic={}

for i in arr:'''

dic={1:"rahul",2:"annaldas"}

for i in dic:
    print(i)

for j in dic.values():
    print(j)

for i,j in dic.items():
    print(f"{i}:{j}")

            