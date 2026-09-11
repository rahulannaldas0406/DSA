def third_smallest(arr):

    #declare variables and assign values 

    third=float('inf')
    second=float('inf')
    smallest=float('inf')

    for curr in arr:

        if curr<smallest: #9<8 false 5<8  0<5 4<0
            third=second#8
            second=smallest #4
            smallest=curr#0 

        elif curr<second and curr!=second: #9<inf true  4<5
            third=second
            second=curr#4
        elif curr<third and curr!=third:
            third=curr

    return third

a=third_smallest([8,9,4,12,25,-6])

print(a)