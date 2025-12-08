#Implement Bubble Sort

#Problem: Write bubble_sort(arr) that sorts arr in ascending order using bubble sort and returns the sorted array.
#Example: [4,2,7,1] → [1,2,4,7]

# def bubble_sort(arr):
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr

# def bubble(arr):
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr)):

#             if arr[i]<arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
                
#     print(arr)

# bubble([4,2,7,1,6])

def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):     # compare until unsorted part
            if arr[j] > arr[j+1]:  # compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
