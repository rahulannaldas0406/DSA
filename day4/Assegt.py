'''Write code for print number of factors'''

'''i=1
n=24
while(n%i==0):
    fac=n//i
    print(i,fac)
    i=i+1'''
'''n=24
for i in range(1,n+1):
    n%i==0'''

'''there is no use of thid logic to build with for loop only.
We can write in for using for loop in that we have put if condition '''

'''Now count the number of factors'''

'''i=1
n=24
count=0
while(n%i==0):
    count=count+1
    i=i+1
print(count)'''


'''Check prime number'''

'''if(23%2==0):
    print("it is not prime number")
else:
    print("It is prime number")'''

'''while(24%2==0):
    print("It is not a prime number")
    break
print("it is prime number")'''

'''in the above problem there have one draw back which means when while condition is true 
then output was print both print statements like in side loop statement and outside statement so it not possible in while loop as well as i tried in diiferent method like switch,if it 
is also not possible  '''

'''print entered given numbers sum of all the numbers'''

'''sum=0
n=int(input("enter a how many numbers you want to sum:"))
for i in range(1,n+1):
    num=int(input("enter random numbers:"))
    sum=sum+num
print(sum)'''

'''using while '''
'''i=1
sum=0
n=int(input("enter how many numbers if you want to sum:"))
while(i<=n):
 num=int(input("enter a random number:"))
 sum=sum+num
 i=i+1
print(sum)'''
'''Yes it working'''

'''sum of all digits of a given number Ex: let us take 19345 is the given number The output should be 22 (1+9+3+4+5)=22'''
'''sum=0
n=19345
while(n>0):
    temp=n%10
    sum=sum+temp
    n=n//10
print(sum)'''

'''using for loop'''

'''sum=0
n=129834
for i in str(n):
     sum=sum+int(i)
print(sum)'''

'''Also we can write in short space complexity for example'''

'''n = 54321
digit_sum = sum(int(d) for d in str(n))
print("Sum of digits:", digit_sum)'''

'''a program to print reverse of digits of a number'''

'''n=123
rev=0
while(n>0):
    temp=n%10
    n=n//10
    rev=rev*10+temp
print(rev)'''

n = 12345

# Step 1: Count digits
temp = n
count = 0
while temp > 0:
    temp //= 10
    count += 1
print(count)



    