#Print A Calendar Taking Input From User Using Loop

'''for i in range(1,32):
    print(i,end=" ")
    if i%7==0:
        print()'''
'''month=input("Enter a month:")


match month:
    case 'january':
        for i in range(1,32):
            print(i,end=" ")
            if i%7==0:
                print()
    case 'february':
        for i in range(1,29):
            print(i,end=" ")
            if i%7==0:
                print()
    case 'march':
        for i in range(1,32):
            print(i,end=" ")
            if i%7==0:
                print()
    case '''

# cel=[0,12,34]
# value=map(lambda c:(c*9/5)+32,cel)
# print("ferhaint:",list(value))


#Remove All Vowels From A String
'''n="asjfi nowninnoij"
vow='aeiouAEIOU'
result=0
count=0
for char in n:
    if char not in vow:
        count+=1
    else:
        result+=1
print("constants are:",count)
print("Vowels are:",result)'''

name="ArAdY@123"
small="abcdefghijklmnopqrstuvwxyz"
big="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sc="!@#$%^&*()_-+=><;:?/"
dg="1234567890"
for char in name,small,big,sc,dg:
    print(char)
        