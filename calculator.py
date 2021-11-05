#this function adds two numbers
def add(x,y):
    return x+y

#this function subtracts two numbers
def subtract(x,y):
    return x-y

#this function multiplies two numbers
def multiply(x,y):
    return x*y

#this function divides two numbers
def divide(x,y):
    return x/y

#print possible selections for calculator input types
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #take input from user
    choice = input("Enter choice(1/2/3/4): ")

    #check if choice is one of the options
    if choice in ('1','2','3','4'):
        a = float(input("Enter first number: "))
        d = float(input("Enter second number:"))

        if choice == '1':
            print(a, "+", d, "=", add(a,d))

        elif choice == '2':
            print(a, "-", d, "=", subtract(a,d))

        elif choice == '3':
            print(a, "+", d, "=", multiply(a,d))

        elif choice == '4':
            print(a, "/", d, "=", divide(a,d))

        #check if user wants another calculation
        #break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (Y/N): ")
        if next_calculation == "N":
            break
    #otherwise print invalid choice
    else:
        print("Invalid choice!")
        
