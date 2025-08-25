# t=4
# n=6
# i=1
# pow=n
# while(i<t):
#    pow= pow*n
#    i=i+1
# print(pow)

#just for fun 
'''value="yes"
while(value=="yes"):
    n=int(input("enter a number:"))
    t=int(input("enter power of the number:"))
    pow=1
    for i in range(0,t):
        pow=pow*n
    print(pow)
    value=input("you want to repeat say yes/no:")
print("thank you for your concern :)")'''


#Project Idea: Number Guessing with Binary Search

low,high=1,100
while low<=high:
    mid=(low+high)//2
    print("Is it",mid,"?:")
    feedback=input("enter if higher/lower/correct:")
    if feedback=="correct":
        print("i guessed correct it 🎉")
        break
    elif feedback=="higher":
        low=mid+1
    else:
        high=mid-1
