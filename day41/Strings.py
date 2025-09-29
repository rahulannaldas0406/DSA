#Write a program to convert a sample sentence string into an array of all the words in the sentence.
#  Example: Input->‘Hello World’; Output->[‘Hello’,‘World’]

n=5


for i in range(1,n+1):
    for k in range(0,n-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
