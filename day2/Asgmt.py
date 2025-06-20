'''Greatest number using switch case'''
a,b=map(int,input("enter any two number:").split())
num=(int(a),int(b))
match num:
    case _ if a>b:
      print("a is greatest")
    case _ if a<b:
      print("b is greatest")
    case _ if a==b:
        print("both equal") 





'''Write a program to take marks of three subjects and print the grade of student'''


'''maths,scie,chem=map(int,input("enter Three subjects marks:").split())
avg=int(maths)+int(scie)+int(chem)'''
'''if(avg==300):
    print("Grade O")
elif(avg>=250 & avg<300):
    print("Grade A+")
elif(avg>=200 & avg<250):
    print("Grade A")
elif(avg>=150&avg<200):
    print("Grade B+")
elif(avg>=100&avg<150):
    print("Grade B")
elif(avg>=50&avg<100):
    print("Grade C")
elif(avg>=0&avg<50):
    print("Fail")'''

#Using switch
'''match avg:
    case avg==300:
      print("Grade O")
    case avg>=250 & avg<300:
      print("Grade A+")
    case avg>=200 & avg<250:
      print("Grade A")
    case avg>=150&avg<200:
      print("Grade B+")
    case avg>=100&avg<150:
      print("Grade B")
    case avg>=50&avg<100:
      print("Grade C")
    case avg>=0&avg<50:
      print("Fail")
       there is no use bitwise operator in cases instead use logical operator
      
      '''
'''match avg:
    case 300:
        print("Grade O")
    case _ if 250 <= avg < 300:
        print("Grade A+")
    case _ if 200 <= avg < 250:
        print("Grade A")
    case _ if 150 <= avg < 200:
        print("Grade B+")
    case _ if 100 <= avg < 150:
        print("Grade B")
    case _ if 50 <= avg < 100:
        print("Grade C")
    case _ if 0 <= avg < 50:
        print("Fail")
    case _:
        print("Invalid marks")'''



