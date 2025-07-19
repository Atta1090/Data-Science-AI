# A function is block of code that only runs when it is called.
# A function can take arguments, which are values that are passed to the function when it is called
# A function can return a value, which is the output of the function when it is called

#without paramters
def greet_User():
    print("Hello user")
greet_User()

#with parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Muhammad Attaulah")

def name(a = "Atta"):
    print(a)
name()