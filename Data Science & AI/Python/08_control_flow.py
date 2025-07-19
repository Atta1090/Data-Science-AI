# conditional statement
# <, >, <=, >=, ==, !=
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# for loops
fruits = ['Apple', 'Mango', 'Banana', 'Grapes', 'Pineapple']
for fruit in fruits:
    print(fruit)

# while loop
i = 0
while i < 5:
    print(i)
    i = i+1

#control statement
for letter in "python":
    if letter == "h":
        break
    print(letter)  
    
for letter in "python":
    if letter == "h":
        continue
    print(letter)  

for letter in "python":
    if letter == "h":
        pass
    print(letter)  