# PLP Week 8 Final Project
# Personal Mini-Toolkit


# Tool 1: Simple Calculator
# Allows the user to perform basic mathematical operations.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter your operation: ")

        if operation == "1":
            result = number1 + number2
            print(f"Result: {result}")

        elif operation == "2":
            result = number1 - number2
            print(f"Result: {result}")

        elif operation == "3":
            result = number1 * number2
            print(f"Result: {result}")

        elif operation == "4":
            if number2 == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = number1 / number2
                print(f"Result: {result}")

        else:
            print("Invalid operation. Please choose 1, 2, 3, or 4.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List
# Allows the user to add tasks and view the tasks in a list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"Task added: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")

            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Tool 3: Pass Checker
# Checks whether a learner has passed or failed based on their score.
def pass_checker():
    print("\n--- Pass Checker ---")

    try:
        score = float(input("Enter your score: "))

        if score >= 50:
            print(f"Your score is {score}. Congratulations, you passed!")

        elif score >= 0:
            print(f"Your score is {score}. Unfortunately, you failed.")

        else:
            print("Score cannot be negative.")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
# Keeps displaying the menu until the user chooses to quit.
def main():
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n===== PERSONAL MINI-TOOLKIT =====")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Pass Checker")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            pass_checker()

        elif choice == "4":
            print("Thank you for using the Personal Mini-Toolkit!")
            print("Goodbye!")
            break

        else:
            print("Sorry, that is not a valid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()