#selection sort aproach

'''
1.Assume current position has minimum
2.Find smallest element in remaining array
3.Swap once
4.Move to next position'''

#Code
def selection_sort(arr):

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

