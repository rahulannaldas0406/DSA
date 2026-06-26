#basic insertion sort structure 
'''arr=[5,3,4,2]
for i in range(1,len(arr)):

    key=arr[i]

    j=i-1

    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]

        j-=1


    arr[j+1]=key

print(arr)'''


#Sort array in descending order

'''def sort_scores(scores):

    for i in range(1, len(scores)):

        key = scores[i]

        j = i - 1

        while j >= 0 and scores[j] < key:

            scores[j + 1] = scores[j]

            j -= 1

        scores[j + 1] = key

    return scores


print(sort_scores([450, 800, 300, 1000, 600]))'''

#Print array after each pass

'''def print_each_pass(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

        print("Pass", i, ":", arr)


print_each_pass([5, 3, 4, 1])'''

#Count number of shifts

'''def count_shifts(arr):

    shifts = 0

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            shifts += 1

            j -= 1

        arr[j + 1] = key

    return shifts


print(count_shifts([5, 3, 4, 1]))'''

#Count number of comparisons

'''def count_comparisons(arr):

    comparisons = 0

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0:

            comparisons += 1

            if arr[j] > key:

                arr[j + 1] = arr[j]

                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons


print(count_comparisons([5, 3, 4, 1]))'''

#Print total passes required
'''def total_passes(arr):

    if len(arr) <= 1:
        return 0

    return len(arr) - 1


print(total_passes([5, 3, 4, 1]))'''

#Find inserted position of key each pass


'''def inserted_position(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

        print(
            "Pass", i,
            ": Key =", key,
            "inserted at index", j + 1
        )


inserted_position([5, 3, 4, 1])'''

#Print key element each pass 

'''def print_key_each_pass(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        print("Pass", i, ": Key =", key)

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key


print_key_each_pass([5, 3, 4, 1])'''


#Sort already sorted array

'''def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([1, 2, 3, 4]))'''


#Sort reverse sorted array


'''def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([5, 4, 3, 2, 1]))'''

#Sort array with duplicates

'''def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([4, 2, 5, 2, 3]))'''


#Sort array with negative numbers

'''def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([-3, 5, -7, 2, -1]))'''

#Sort array with zeros

'''def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([4, 0, 2, 0, 1]))'''

#Sort array with all equal elements

'''def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([7, 7, 7, 7]))'''


#Sort only first half of array


'''def first_half_sort(arr):

    n = len(arr) // 2

    for i in range(1, n):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(first_half_sort([8, 4, 6, 2, 9, 1]))'''

#Sort only second half of array

'''def second_half_sort(arr):

    start = len(arr) // 2

    for i in range(start + 1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= start and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


print(second_half_sort([8, 4, 6, 2, 9, 1]))'''

#Sort first K elements

'''def first_k(arr,k):
    for i in range(1,k):
        key=arr[i]

        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]

            j-=1

        arr[j+1]=key
    return arr
arr=[9, 7, 5, 3, 1]
k=3
print(first_k(arr,k))'''

#Sort Except First Element

'''def except_first(arr):
    for i in range(2,len(arr)):
        key=arr[i]
        j=i-1

        while j>=1 and arr[j]>key:
            arr[j+1]=arr[j]

            j-=1
        arr[j+1]=key

    return arr
arr=[10, 5, 8, 2, 7]
print(except_first(arr))'''

#Sort Except Last Element 

'''def except_last(arr):
    for i in range(1,len(arr)-1):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]

            j-=1
        arr[j+1]=key
    return arr
arr=[10, 7, 8, 6, 5]
print(except_last(arr))'''

#Sort Only Positive Numbers

def positve_ele(arr):
    for i in range(1,len(arr)):
        if arr[i]>=0:
            key=arr[i]

            j=i-1
            while j>=0 and arr[j]>key and arr[j]>=0: #0 1 2 3 
                arr[j+1]=arr[i]

                j-=1
    
            arr[j+1]=key
    return arr

arr=[4, -1, 2, -5, 1]
print(positve_ele(arr))