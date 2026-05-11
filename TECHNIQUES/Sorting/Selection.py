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

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)


selection_mxd([3,8,-5,-7,-1,2,-4,0])'''

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

    # Selection Sort
    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if needed
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