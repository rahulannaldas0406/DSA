#selection sort aproach

'''
1.Assume current position has minimum
2.Find smallest element in remaining array
3.Swap once
4.Move to next position'''

#Code
def selection_sort(arr):

    count_swaps=0
    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        

    
    print(arr)


selection_sort([3,8,5,7,1,2,4,0])


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


selection_sort([1,2,3,4,5])'''

