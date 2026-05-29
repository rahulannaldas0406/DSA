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