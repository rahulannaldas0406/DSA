#Write a function which can return the sum of two numbers.
'''function add(a,b){
 …………………
}
 var sum = add(45,67);
    console.log(sum);
//Expected output: 112'''

'''def add(a,b):
    print(a+b)

add(2,4)'''

'''def sum(a,b):
    return a+b
add=sum(2,4)
print(add)'''

#Write a function which can return the greatest of the three numbers passed in arguments.
'''function compare(a,b,c){ 
            …………………
    }
    var greatest = compare(45,67,23);
    console.log(greatest);//67'''

'''def gNum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
value=gNum(4,0,1)
print(value)'''

#Write a function which can print the given arguments in ascending order.
'''function sortNums(a,b,c){
    …………………
    }
    var ascending = sortNums(45,7,68);
    console.log(ascending);//'''                           
                            

def print_ascending_dsa(*args):
    arr = list(args)   # convert tuple to list
    
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap
    
    # print result
    for val in arr:
        print(val)
print_ascending_dsa(4,5,2,3,1)

