#Initializing variables
hours=0
minutes=0
seconds=0
Finalvalueinseconds=0

#Tracking user inputs
hours=float(input("Enter the number of hours"))
minutes=float(input("Enter the number of minutes"))
seconds=float(input("Enter the number of seconds"))

#Calculate the total value in seconds
Finalvalueinseconds=hours*60*60+minutes*60+seconds

#Display Final value in seconds
print("Final value in seconds is",Finalvalueinseconds)
