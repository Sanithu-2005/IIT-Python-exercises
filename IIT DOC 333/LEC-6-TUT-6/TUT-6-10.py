#Intializing variables
grams_of_fat=0
grams_of_carbo=0
grams_of_protein=0
Total=0

#Tracking user inputs
grams_of_fat=float(input("Enter the number of grams of fat"))
grams_of_carbo=float(input("Enter the number of grams of carbohydrates"))
grams_of_protein=float(input("Enter the number of grams of protein"))

#Calculate the total number of calories
Total=grams_of_fat*9+grams_of_carbo*4+grams_of_protein*4

#Display the total number of calories
print("The total number of calories is",Total)
