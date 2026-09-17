##Basic Level (Star Patterns)
#Right-angled triangle
for space range(1,2):
    print("\t")
    for i in range(0,5):
        for j in range(1,i+1):
            print(j,end=" ")
        print("")

#using while loop

'''i=1
while(i<=5):
    j=i+1
    while(j>i):
        print(i,end=" ")
        j=j-1
    i=i+1
    print()'''


#Repeating row numbers

'''for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()'''
'''i=0
n=4
while(n>0):
    j=i+1
    while(j>0):
        print(i+1,end=" ")
        j=j-1
    print()
    i=i+1
    n=n-1'''

#Reverse numbers
#
'''for i in range(5,0,-1):
    #print(i,end=" ")
    for j in range(5,5-i,-1):
        print(j,end=" ")
    print()'''
#using while loop

'''i=0
while i<5:
    j=5
    while j>i:
        print(j,end=" ")
        j=j-1
    print()
    i=i+1'''





