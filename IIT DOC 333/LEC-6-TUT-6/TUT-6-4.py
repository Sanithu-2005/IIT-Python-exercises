#Calling math function
import math

#Creating and Intializing variables
radius=0
height=0
area=0

#Taking user inputs
radius=float(input("Enter radius of a cone"))
height=float(input("Enter the height of a cone"))

#Calculating area of a circle
area=math.pi*radius*(radius+math.sqrt((height*height)+(radius*radius)))

#Display the area
print("Area of a circle",area)
                     
                     
