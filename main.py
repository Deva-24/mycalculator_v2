from app.calculator import Calculator

def main():
    calc = Calculator()

    while True:
        print("\n *** Calculator_V2 ***")
        print("\n Choose an operation to perform (1-8):")
        print(" 1: Addition")
        print(" 2: Subtract")
        print(" 3: Multiply")
        print(" 4: Divide")
        print(" 5: Modulus")
        print(" 6: Power")
        print(" 7: View History")
        print(" 8: Quit")
        
        operation = input("\n Enter the number(1-8) to perform : \n ").strip()

        if operation == "8":
            print("Bye Bye")
            break

        if operation == "7":
            history_choice = input("View (1) full history or (2) last operation? ")
            if history_choice == '1':
                print("\n".join(calc.get_history()))
            elif history_choice == '2':
                print("\n".join(calc.get_history(last_only=True)))
            continue

        if operation in {"1", "2", "3", "4", "5", "6"}:
            try:
                a = float(input("Enter 1st Number: "))
                b = float(input("Enter 2nd Number: "))
                
                if operation == "1":
                    result = calc.perform_operation("add", a, b)
                elif operation == "2":
                    result = calc.perform_operation("subtract", a, b)
                elif operation == "3":
                    result = calc.perform_operation("multiply", a, b)
                elif operation == "4":
                    result = calc.perform_operation("divide", a, b)
                elif operation == "5":
                    result = calc.perform_operation("modulus", a, b)
                elif operation == "6":
                    result = calc.perform_operation("power", a, b)

                print(f"Result: {result}")

            except ValueError as e:
                print(f"Error: {e}")

        else:
            print("Invalid operation. Enter proper value.")

if __name__ == "__main__":
    main()
