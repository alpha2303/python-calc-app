from .entry_handlers import IntegerEntryHandler, ComplexEntryHandler

operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x - y,
    3: lambda x, y: x * y,
    4: lambda x, y: x / y,
}

entry_handlers = {
    1: IntegerEntryHandler.get_input,
    2: ComplexEntryHandler.get_input,
}

if __name__ == "__main__":
    print("Welcome to Calculator!")
    while True:
        # Step 1: Choose type of math operation from given options
        print("\nChoose Operation: ")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Exit")
        
        # input fn returns string value, which is 'type-casted' to int datatype
        choice = int(input("Enter choice of operation: ")) 
        
        # Break loop if exit is chosen
        if not choice: # zero int value of choice variable is treated as False value -> "not choice" will be True
            break

        if choice not in operations.keys():
            print("ERROR - Invalid operation choice.")
            continue

        print("Choose Datatype: ")
        print("1. Integer")
        print("2. Complex Number")
        type_choice = int(input("Enter choice of datatype: "))

        if type_choice not in entry_handlers.keys():
            print("ERROR - Invalid type choice")
            continue

        # using dictionary is a good way to handle multple cases in Python (switch statement)
        print("Enter Operand 1 ->")
        value1 = entry_handlers[type_choice]()
        print("Enter Operand 2 ->")
        value2 = entry_handlers[type_choice]()
        try:
            result = operations[choice](value1, value2)
            print("\nResult: " + result.to_string() +"\n")
        except ZeroDivisionError as e:
            print(f"Division by Zero not allowed. Operation performed: {value1.to_string()} / {value2.to_string()}")
    
    print("Exiting...")
    print("\n *** Thank you! *** \n")