# name = input()
# print('name: ',name)

# a = input('what is your name person A')
# b = input('what is your name peron B')
# a1 = input('Person A Age')
# b1 = input('Person B Age')

# if a1>b1:
#     print(a,'is older than',b)
# else:
#     print(b,'is older than',a)
person_A = input("Enter your name: ")
person_height_cm = float(input("Enter your height in cm: "))
person_weight_kg = float(input("Enter your weight in kg: "))

# Convert height to meters
person_height_m = person_height_cm / 100

# Calculate BMI
bmi = person_weight_kg / (person_height_m ** 2)

# Display result
print(f"{person_A}, your BMI is: {bmi:.2f}")
