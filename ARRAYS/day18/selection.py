#patterns

'''for i in range(0,6):
    for j in range(i,7):
        if i==j:
            print(end=" ")
        else:
            print("*",end=" ")
    print()'''

'''rows=5
for i in range(rows):
    print(" "*i+"*"*(rows-i))'''

'''for i in range(5,-1,-1):
    print(i)'''

for i in range(0,6):
    for k in range(0,i):
        print(" ",end="")
    for j in range(0,6-i):
        # print(""*i)
        print("*",end="")
    print()
    
# for i in range(5,0,-1):
#     print(" "* (5-i)+"*" * i)