#Types of argument

'''def default(x,y=10):
    print("x:",x)
    print("y:",y)
default(10)'''

'''def even(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"

print(even(2))
print(even(3))'''

'''def myFun(*a):
    for i in a:
        print(i)
myFun("hello","welcome","to","coding","journey")'''

'''a=["rahul","das","annaldas"]
for i in a:
    print(a)'''

'''def myFun(**a):
    for i,j in a.items():
        print(f"{i}=={j}")
myFun(first='Rahul',mid='das',last='annaldas')'''


'''x=20
def show():
    x=10
    print("Inside function x=",x)
    #print("outside function y=",y)
show()
print("outside function x=",x)'''

#nonlocal variable with nested functions

'''def outer():
    x=10
    def inner():x   
        y=x
        y+=1
        print("inside y=",y)
    inner()
    print("outside x=",x)
outer()'''



'''def sum():
    mssg="messg"
    def inner():
        mssg="hi"
        pass
    inner()
    print("mssg:",mssg)
sum()'''

#lambda function

#Example 1

'''add=lambda a,b:a+b
print(add(2,3)) '''#output:5

#example 2

'''square=lambda a:a*a
print(square(4))'''#output:16

#example 3

'''max=lambda a,b:a if a>b else b
print(max(10,20))'''#output:20

'''nums=[1,2,3,4]
square=list(map(lambda x:x*x,nums))
print(square)'''#output:[1,4,9,16]

#example 4

'''nums=[1,2,3,4,5,6,7,8]
even=list(filter(lambda x:x%2==0,nums))
print(even)'''#output:[2,4,6,8]

#example 5

'''students=[("rahul",92),("jhon",89),("neha",73),("yogith",90)]
sorted_students=list(sorted(students,key=lambda x:x[1]))
print(sorted_students)'''#[('neha', 73), ('jhon', 89), ('yogith', 90), ('rahul', 92)]

'''arr=[2,5,3,6,53,22,60,21,11,63]
sorted=sorted(arr)
print(sorted)'''

n = 12
binary = ""

while n > 0:
    rem = n % 2
    print(f"{n} % 2 = {rem}")
    binary = str(rem) + binary
    n = n // 2
    print(f"New n = {n}, binary so far = {binary}")

print("Final binary:", binary)

