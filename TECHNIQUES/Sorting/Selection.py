#selection sort aproach

'''
1.Assume current position has minimum
2.Find smallest element in remaining array
3.Swap once
4.Move to next position'''

#Code
'''def selection_sort(arr):

    count_swaps=0
    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        

    
    print(arr)


selection_sort([3,8,5,7,1,2,4,0])'''


#Sort an array in ascending order

'''def selec_asc(arr):
    for i in ramge(len(arr)):
        min_index=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]
            min_index=j
        
        arr[i],arr[min_index]=arr[min_index],arr[i]

    print(arr)

selec_asc([3,8,5,7,1,2,4,0])''' #[0,1,2,3,4,5,7,8]

#Sort an array in descending order
#(small change where nested for loop in if conditon change less then to greater then)

'''def selec_dsc(arr):
    for i in range(len(arr)):
        min_index=i

        for j in range(i+1,len(arr)):
            if arr[j]>arr[min_index]:
                min_index=j
        
        arr[i],arr[min_index]=arr[min_index],arr[i]

    print(arr)

selec_dsc([3,8,5,7,1,2,4,0])''' #[8, 7, 5, 4, 3, 2, 1, 0]

#Sort array with 5 elements

'''def selec_fiv(arr):
    for i in range(len(arr)):
        min_index=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        
        arr[i],arr[min_index]=arr[min_index],arr[i]

    print(arr)

selec_fiv([3,1,2,4,0])'''

#Sort array with 10 elements 

'''def selec_ten(arr):
    for i in range(len(arr)):
        min_index=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        
        arr[i],arr[min_index]=arr[min_index],arr[i]

    print(arr)

selec_ten([3,8,5,7,1,2,4,0])'''


#Sort array with duplicate elements

'''def selection_dup(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)


selection_dup([7, 3, 7, 1, 7])'''

#Sort array with all equal elements

'''def selection_eql(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)


selection_eql([3, 3, 3, 3, 3, 3])'''

#Sort array with negative numbers

'''def selection_neg(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)


selection_neg([-3, -1, -7, -4, -5])'''

#Sort array with positive numbers

'''def selection_pov(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)


selection_pov([3,8,5,7,1,2,4,0])'''


#Sort array with mixed positive and negative numbers

'''def selection_mxd(arr):
    count=1
    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        if min_index!=i:
            count+=1

    print(arr)
    print(count)


selection_mxd([1,2,3,4,5])'''

# num=[2,3,4,5,1]
# num.sort()
# print(num)
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
index=0
for item in arr2:
    for i in range(index,len(arr1)):
        if item == arr1[i]:
            arr1[index],arr1[i] = arr1[i],arr1[index]
            index += 1
print(arr1)
print(arr2)
print(index)
#Count number of comparisons

'''def selection_comp(arr):

    comparisons = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):

            comparisons += 1   # Count comparison

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print("Sorted:", arr)
    print("Comparisons:", comparisons)


selection_comp([3,8,5,7,1,2,4,0])'''

#Count number of swaps

'''def selection_swap(arr):

    swaps = 0

    for i in range(len(arr)):

        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    print("Sorted:", arr)
    print("Swaps:", swaps)


selection_swap([3,8,5,7,1,2,4,0])'''

#Print array after each pass

'''def selection_each(arr):

    for i in range(len(arr) - 1):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

        print("Pass", i+1, ":", arr)


selection_each([3,8,5,7,1,2,4,0])'''

#Find minimum element in array

'''def find_min(arr):

    if len(arr) == 0:
        return "Array is empty"

    min_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]

    return min_value
    
print(find_max([3,8,5,7,1,2,4,0]))'''

#Find maximum element using selection logic

'''def find_max(arr):

    max_value = arr[0]   # assume first element is maximum

    for i in range(1, len(arr)):

        if arr[i] > max_value:
            max_value = arr[i]

    return max_value


print(find_max([3,8,5,7,1,2,4,0]))'''


#Sort already sorted array

'''def selection_sort(arr):

    swaps = 0

    for i in range(len(arr) - 1):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print("Pass", i+1, ":", arr)

    print("Total swaps:", swaps)
    return arr


selection_sort([1,2,3,4,5])
'''

#Sort array in reverse order

'''def selection_sort_desc(arr):

    n = len(arr)

    for i in range(n - 1):

        max_index = i   # assume current is maximum

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:   # change sign here
                max_index = j

        # Swap if needed
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

        print("Pass", i+1, ":", arr)

    return arr


selection_sort_desc([3,8,5,7,1,2,4,0])'''

#Find second smallest element

'''def sec_smallest(arr):
    

    if len(arr)< 2:
        return "Array too small"
    

    smallest=float('inf')
    second=float('inf')

    for i in arr:
        if i <smallest:
            second=smallest
            smallest=i

        elif i <second and i!=smallest:
            second=i
        
    if second==float('inf'):
        return "No second smallest"
        

    return second
    

arr=[2,3,4,1,5]
a=sec_smallest(arr)

print(a)'''

#Find second largest element


'''def sec_large(arr):

    large=float('-inf')
    sec_largest=float('-inf')

    for i in arr:

        if i>large:
            sec_largest=large
            large=i
        elif i>sec_largest and i!=large:
            sec_largest=i

    return sec_largest

print(sec_large([5,1,2,3,4]))'''


#Find third smallest element

'''def third_smallest(arr):
    

    if len(arr)< 2:
        return "Array too small"
    

    smallest=float('inf')
    second=float('inf')
    third=float('inf')

    for i in arr:
        if i <smallest:
            third=second
            second=smallest
            smallest=i

        elif i <second and i!=smallest:
            second=i

        elif i<third and i!=second and i!=smallest:
            third=i


        
    if third==float('inf'):
        return "No second smallest"
        

    return third
    

arr=[2,3,4,1,5]
a=third_smallest(arr)

print(a)'''


#Find third largest element

'''def third_largest(arr):
    third=float('-inf')
    second=float('-inf')
    largest=float('-inf')

    for num in arr:
        if num>largest:
            third=second
            second=largest
            largest=num

        elif num>second and num!=largest:
            third=second
            second=num
            
        elif num>third and num!=second and num!=largest:
            third=num

    return third

a=third_largest([-5,6,7,-3,2])

print(a)'''

#Sort only first half of array

'''def half_sort(arr):


    n=len(arr)//2

    for i in range(n-1):

        min_index=i

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr        
        
a=half_sort([8, 4, 6, 2, 9, 1])

print(a)'''


#Sort only second half of array


'''def half_sort(arr):

    n=len(arr)//2

    for i in range(n,len(arr)):

        min_index=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr        
        
a=half_sort([8, 4, 6, 2, 9, 1])

print(a)'''


#Sort first K elements

'''def selection_sort(arr,k):

    for i in range(k-1):

        min_index=i

        for j in range(i+1,k):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

a=selection_sort([5,3,2,4,6,1],4)

print(a)'''


#Find Kth smallest element

'''def kth_smallest(arr, k):

    n = len(arr)

    if k <= 0 or k > n:
        return "Invalid K"

    for i in range(k):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr[k - 1]


print(kth_smallest([7,3,9,1,5], 2))'''


#Find Kth largest element


'''def kth_largest(arr, k):

    n = len(arr)

    if k <= 0 or k > n:
        return "Invalid K"

    for i in range(k):

        max_index = i

        for j in range(i + 1, n):

            if arr[j] > arr[max_index]:
                max_index = j

        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr[k - 1]


print(kth_largest([7,3,9,1,5], 2))'''


#Sort array of characters

'''def char_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = char_sort(['d', 'a', 'c', 'b'])

print(a)'''


#Sort string characters  


'''def sort_string(s):

    arr = list(s)

    n = len(arr)

  
    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return ''.join(arr)


a = sort_string("dcba")

print(a)'''


#Sort array of lowercase letters


'''def sort_lowercase(arr):

    n = len(arr)

    
    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = sort_lowercase(['d', 'a', 'c', 'b'])

print(a)'''

#Sort array of uppercase letters


'''def sort_uppercase(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = sort_uppercase(['D', 'A', 'C', 'B'])

print(a)'''

#Sort array with zeros included

'''def selection_sort(arr):

    count_swaps=0
    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        

    
    print(arr)


selection_sort([4, 0, 2, 4, 0, 1])'''


#Sort array ignoring negative numbers

'''def selection_sort(arr):

    count_swaps=0
    for i in range(len(arr)):

        min_index = i
        if arr[min_index]>=0:
            for j in range(i + 1, len(arr)):
                if arr[j]>=0:
                    if arr[j] < arr[min_index]:
                        min_index = j
        
        if min_index!=i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        

    
    print(arr)


selection_sort([0, -1, 4, 2])'''


#Sort only positive numbers


'''def selection_sort_positive(arr):

    for i in range(len(arr) - 1):

        min_index = i

        # Process only positive positions
        if arr[min_index] > 0:

            for j in range(i + 1, len(arr)):

                # Compare only positive numbers
                if arr[j] > 0 and arr[j] < arr[min_index]:
                    min_index = j

        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_positive([0, 5, 3, 0, 1])

print(a)'''


#Sort only even numbers

'''def selection_sort_even(arr):

    for i in range(len(arr) - 1):

        min_index = i

        
        if arr[min_index] % 2 == 0:

            for j in range(i + 1, len(arr)):

                if arr[j] % 2 == 0 and arr[j] < arr[min_index]:
                    min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_even([4, 3, 2, 1, 6])

print(a)'''

#Sort only odd numbers

'''def selection_sort_even(arr):

    for i in range(len(arr) - 1):

        min_index = i

        
        if arr[min_index] % 2 != 0:

            for j in range(i + 1, len(arr)):

                if arr[j] % 2 != 0 and arr[j] < arr[min_index]:
                    min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_even([4, 3, 2, 1, 6])

print(a)'''


#Sort numbers divisible by 3

'''def selection_sort_even(arr):

    for i in range(len(arr) - 1):

        min_index = i

        
        if arr[min_index] % 3 == 0:

            for j in range(i + 1, len(arr)):

                if arr[j] % 3 == 0 and arr[j] < arr[min_index]:
                    min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_even([9, 2, 6, 1, 3])

print(a)'''

#Sort numbers divisible by 5

'''def selection_sort_even(arr):

    for i in range(len(arr) - 1):

        min_index = i

        
        if arr[min_index] % 5 == 0:

            for j in range(i + 1, len(arr)):

                if arr[j] % 5 == 0 and arr[j] < arr[min_index]:
                    min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_even([9,10,5,3,0,25])

print(a)'''

#Sort numbers greater than 10

'''def selection_sort_even(arr):

    for i in range(len(arr) - 1):

        min_index = i

        
        if arr[min_index] >10:

            for j in range(i + 1, len(arr)):

                if arr[j] >10 and arr[j] < arr[min_index]:
                    min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_even([9,10,5,30,0,25])

print(a)'''


#Sort numbers less than 50

'''def selection_sort_even(arr):

    for i in range(len(arr) - 1):

        min_index = i

        
        if arr[min_index] <50:

            for j in range(i + 1, len(arr)):

                if arr[j] >50 and arr[j] < arr[min_index]:
                    min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_even([9,10,5,30,0,25])

print(a)'''

#Sort array except first element

'''def first_element(arr):
    
    for i in range(1,len(arr)):

        min_index=i

        for j in range(i+1,len(arr)):

            if arr[j]<arr[min_index]:
                min_index=j

        if arr[i]!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

a=first_element([4,3,5,6,2,1])

print(a)'''

#Sort array except last element

'''def last_element(arr):

    for i in range(len(arr)-1):

        min_index=i

        for j in range(i+1,len(arr)-1):
            if arr[j]<arr[min_index]:
                min_index=j

        if arr[i]!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]


    return arr

a=last_element([4,5,6,2,1,3])
print(a)'''

#Find smallest element in each pass


'''def smallest_each_pass(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        print(f"Pass {i+1} Smallest:", arr[min_index])

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


smallest_each_pass([5, 4, 3, 2, 1])'''

#Find total passes required

'''def total_passes(arr):

    if len(arr) <= 1:
        return 0

    return len(arr) - 1


print(total_passes([5, 4, 3, 2, 1]))'''


#Print index of minimum element each pass

'''def min_index_each_pass(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        print(f"Pass {i+1} Min Index:", min_index)

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


min_index_each_pass([5, 4, 3, 2, 1])'''


#Sort array of strings

'''def selection_sort_strings(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = selection_sort_strings(["banana", "apple", "cherry"])

print(a)'''


#Sort array by string length

'''def sort_by_length(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if len(arr[j]) < len(arr[min_index]):
                min_index = j

        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = sort_by_length(["apple", "kiwi", "banana", "fig"])

print(a)'''

#Find difference between smallest and largest

'''def difference_smallest_largest(arr):

    if len(arr) == 0:
        return "Array is empty"

    smallest = arr[0]
    largest = arr[0]

    for i in range(1, len(arr)):

        if arr[i] < smallest:
            smallest = arr[i]

        if arr[i] > largest:
            largest = arr[i]

    return largest - smallest


a = difference_smallest_largest([5, 2, 8, 1, 9])

print(a)'''

#Sort 2 arrays separately

'''def selection_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr1 = [5, 2, 8]
arr2 = [9, 1, 4]

print(selection_sort(arr1))
print(selection_sort(arr2))'''

#Merge two sorted arrays after selection sort

'''def selection_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def merge_sorted_arrays(arr1, arr2):

    
    arr1 = selection_sort(arr1)
    arr2 = selection_sort(arr2)

    merged = []
    i = 0
    j = 0

    
    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

   
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


arr1 = [5, 2, 8]
arr2 = [9, 1, 4]

print(merge_sorted_arrays(arr1, arr2))'''

#Sort rows of 2D array

'''def selection_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def sort_rows(matrix):

    for i in range(len(matrix)):

        matrix[i] = selection_sort(matrix[i])

    return matrix


matrix = [
    [3, 1, 2],
    [9, 5, 7]
]

print(sort_rows(matrix))'''

#Sort columns of 2D array

'''def sort_columns(matrix):

    rows = len(matrix)#2

    if rows == 0:
        return matrix

    cols = len(matrix[0])#[8,4,6]

    # Column-wise selection sort
    for col in range(cols):

        for i in range(rows - 1):

            min_index = i

            for j in range(i + 1, rows):

                if matrix[j][col] < matrix[min_index][col]:
                    min_index = j

            # Swap column values
            if min_index != i:
                matrix[i][col], matrix[min_index][col] = (
                    matrix[min_index][col],
                    matrix[i][col]
                )

    return matrix


matrix = [
    [8, 4, 6],
    [2, 9, 1]
]

print(sort_columns(matrix))'''

'''arr=[10,5,10,15,10,5]

count={}

for i in range(len(arr)):
    if arr[i]  in count:
        count[arr[i]]+=1
    else:
        count[arr[i]]=1

print(count)

for key,values in count.items():
    print(key,values)'''


# matrix = [
#     [8, 4, 6],
#     [2, 9, 1]
# ]

# print(len(matrix[0]))

