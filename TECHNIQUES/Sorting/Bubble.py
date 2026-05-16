#Basic Bubble sort

'''arr=[5,3,7,2,8,1]

for i in range(len(arr)):

    for j in range(len(arr)-1-i):

        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)'''

#Sort array in descending order


'''def desc_sort(arr):
    n=len(arr)
    for i in range(n):

        for j in range(n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr
a=desc_sort([1,6,4,2,5,3])

print(a)'''


#Print array after each pass

'''def bubble_pass(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

        print("pass",i+1,":",arr)


bubble_pass([5,3,1,4,2])'''

#Count number of swaps

'''def count_swaps(arr):

    count=0

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
    return count
a=count_swaps([6,8,4,2,9,3])

print(a)'''

#Count number of comparisons

'''def count_comp(arr):

    count=0

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            count+=1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return count
a=count_comp([6,8,4,2,9,3])

print(a)'''

#Print total passes required

'''def total_passes(arr):

    return len(arr)-1

print(total_passes([6,5,1,2,3,4]))'''

#Find largest element in each pass

'''def largest_ele(arr):
   
    for i in range(len(arr)):
        
        for j in range(len(arr)-1-i):

            if arr[j]>arr[j+1]:
               
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
        print("Pass", i + 1, "Largest:", arr[len(arr) - 1 - i])
largest_ele([6,8,4,2,9,3])'''

#Print index of largest element each pass

'''def largest_idx(arr):
   
    for i in range(len(arr)):
        
        for j in range(len(arr)-1-i):

            if arr[j]>arr[j+1]:
               
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
        print("Pass", i + 1, "Largest:", len(arr)-1-i)
largest_idx([6,8,4,2,9,3])'''

#Sort already sorted array