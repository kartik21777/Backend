
'''Write a program to input hours and pay per hour. Then find bill(bill = hours*pay). 
If there is a non numeric input use try and except so that your program handles non-numeric input gracefully.

Example for non numeric input-


Enter Hours: 20 
Enter Rate: nine 
Error, please enter numeric input

Enter Hours: forty  
Error, please enter numeric input'''
try:
    pay = float(input("please input pay: "))
    hours = float(input("please input hours: "))
except:
    print("please enter a numeric input")

print("the bill is", str(hours*pay))