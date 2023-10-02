# Python program to check vote eligibility 

age = int(input("Enter age of a user: "))

if age >= 18:
    print("User is eligible for voting: ", age)
else:
    print("User is not eligible for voting: ", age)
