
## greatest of three numbers

""" num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if num1>num2 and num1>num3:
    print("num1 is greatest")
elif num2>num1 and num2>num3:
    print("num2 is greatest")
else:
    print("num3 is greatest")
 """
  


  ### month name from number
"""month=int(input("enter month number:"))
if month==1:
    print("january")
elif month==2:
    print("february")
elif month==3:
    print("march")
elif month==4:
    print("april")
elif month==5:
    print("may")
elif month==6:  
    print("june")
elif month==7:
    print("july")
elif month==8:
    print("august")
elif month==9:
    print("september")
elif month==10:
    print("october")
elif month==11:
    print("number of november")
else:
    print("december") """



    ## swapping of two numbers
'''num1 = int(input("enter a num: "))
num2 = int(input("enter b num: "))
num1, num2 = num2, num1 
print("After swapping:")
print("num1 =", num1)
print("num2 =", num2)'''





 # ticket pricing based on age and membership
'''person = int(input("Enter your age: "))
if person < 12:
    print("Ticket is free")
elif person <= 60:
    membership = input("Are you a member (yes/no): ")
    if membership == "yes":
        price = 150
    else:
        price = 200
    print(f"Ticket price: {price}")
else: 
    price = 100
    print(f"Ticket price: {price}")'''






# electricity bill calculation
'''meow=int(input("enter electricity used in units :"))
if meow<100:
    cost= meow*5
elif meow <=300:
    cost =(100*5)+(meow-100)*8
else:
    cost=(100*5)+(200*8)+(meow-300)*10
print("total electricity bill is:",cost)'''




# rock paper scissor game
''''h=input("enter your move :")
h2=input("enter computer move :")
if h==h2 :
 print("tie")
else:
  if h=="rock":
    if h2=="scissor":
        print(" h win")
    else:
        print("h2 win")
  else:
     if h=="scissor":
        if h2=="rock":
            print("h2 win")
        else:
            print("h win")
     else:
        if h=="paper":
            if h2=="rock":
                print("h win")
            else:
                print("h2 win")
        else:
            print("invalid move") '''





# desk allocation problem
'''a = int(input("Enter students in class A: "))
b = int(input("Enter students in class B: "))
c = int(input("Enter students in class C: "))

desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2

total_desks = desks_a + desks_b + desks_c

print("Total desks needed:", total_desks)'''






# lift movement simulation
'''currentfloor=5
desiredfloor=int(input("enter desired floor:"))
if desiredfloor>currentfloor:
    print("lift goes up")
elif desiredfloor<currentfloor:
    print("lift goes down")
else:
    print("lift stays")'''



# greatest of two numbers
''''num1=int(input("eneter a num:"))
num2=int(input("enter b num:"))
if num1>num2:
    print("num1 is greater than num2")
elif num2>num1:
    print("num2 is greater than num1")  
else:
    print("both are equal")
    if num1 > 0:
        print("positive")
    elif num1 < 0:
        print(" negative")'''



# positive, negative or zero

'''num = float(input("Enter a number: "))

if num > 0:
    if num %2 ==0 :
      print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")'''




# Fizz Buzz problem

'''num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)'''



# random fun fact generator
'''num = random.randint(0,5)
if num == 0:
    print("flaimingos turn pink form eating shrimp")
elif num==1 :
    print("the only food that doesnt spoil is honey")
elif num==2:
        print("shrimp can only swims backwards ")
elif num==3:
     print("A taste bud's life span is about 10 days")
elif num==4:
        print("it is impossible to sneeze with sleeping")
     elif num==5:
            print("it is illegal to sing off key in north carolina")'''



 # discount calculation based on purchase amount and membership
''''num1 = float(input("Total amount of purchase: "))
member = input("Are you a member (yes/no): ")

if num1 > 1000 and member == "yes":
    discount = num1 * 20 / 100
    print("Discount is:", discount)
    final_amount = num1 - discount
    print("Final amount is:", final_amount)

elif num1 > 1000 and member.lower() == "no":
    discount = num1 * 10 / 100
    print("Discount is:", discount)
    final_amount = num1 - discount
    print("Final amount is:", final_amount)

else:
    print("No discount applicable")
    print("Final amount is:", num1) '''





#planet weight
'''
num1 = int(input("Choose a planet number : "))
num2 = float(input("Enter weight on Earth: "))

if num1 == 1:
    gravity = 0.38
    planet = "Mercury"
elif num1 == 2:
    gravity = 0.91
    planet = "Venus"
elif num1 == 3:
    gravity = 0.38
    planet = "Mars"
elif num1 == 4:
    gravity = 2.53
    planet = "Jupiter"
elif num1 == 5:
    gravity = 1.07
    planet = "Saturn"
elif num1 == 6:
    gravity = 0.89
    planet = "Uranus"
elif num1 == 7:
    gravity = 1.14
    planet = "Neptune"
else:
    print("Invalid planet number")
    exit() 
weight_on_planet = num2 * gravity
print(f"Your weight on {planet} would be: {weight_on_planet:}")'''


    
    






























    



    
        





    







 





             
