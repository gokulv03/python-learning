print("Welcome to LOGIC_GATE_SIMULATOR!")
print()

input1 = int(input("Enter first number (0 or 1): "))

input2 = int(input("Enter seccond number (0 or 1): "))

print()
print("Choose a gate: ")
print("1 - AND Gate")
print("2 - OR Gate")
print("3 - XOR Gate")

choice = int(input("Enter your choice(1, 2, or 3): "))

print()
print("Result:")

if choice == 1:
    if input1 == 1 and input2 == 1:
        result = 1
    else:
        result = 0

    print(f"{input1} AND {input2} = {result}")

elif choice == 2:
    if input1 == 1 or input2 == 1:
        result = 1
    else:
        result = 0

    print(f"{input1} OR {input2} = {result}")

elif choice == 3:
    if input1 != input2:
        result = 1
    else:
        result = 0

    print(f"{input1} XOR {input2} = {result}")

else:
    print("Invalid Choice")
    



        
