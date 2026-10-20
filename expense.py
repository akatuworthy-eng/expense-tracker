expense = []

while True :

    print("=== CLI EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total")
    print("q. Quit")

    action = input("CHOOSE AN OPTION (1, 2, 3, q):").strip()
    if action not in ["1", "2", "3", "q"]:
        print("Invalid Action!")
        continue

    if action == "q":
        print("Goodbye!")
        break

    if action == "1":
        description = input("Enter expense description:").strip()
        if description == "":
            print("Space cannot be empty")
            continue
        
        try:
            descriptionamount = float(input("Enter expense amount:").strip())

        except ValueError:
            print("Enter a valid amount!!")
            continue

        if descriptionamount <= 0:
            print("Amount must be greater than zero")
            continue

        new_expense = {

            "description": description,
            "amount": descriptionamount
        }    

        expense.append(new_expense)  

    if action == "2":
        if not expense:
            print("No expenses recorded yet")
        else:
            for number, item in enumerate(expense, start=1):
                print(f"{number}. {item['description']} - ₦{item['amount']:.2f}")

    if action == "3":
        total = 0

        for item in expense:
            total = total + item["amount"]
        
        print(f"Total Expenses: ₦{total:.2f}")