import pickle
from datetime import datetime

class Customer:
    def __init__(self, num, name, date):
        self.num = num
        self.name = name
        self.date = date

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Feedback:
    def __init__(self, customer_num, rating, comment):
        self.customer_num = customer_num
        self.rating = rating
        self.comment = comment
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_customers():
    customers = []
    print('$' * 52 + 'CUSTOMERS' + '$' * 52)
    while True:
        num = int(input("Enter the serial number: "))
        name = input("Enter the name of customer: ")
        date = input("Enter the date of shopping (YYYY-MM-DD): ")
        customers.append(Customer(num, name, date))
        if input("Do you want to store more records? (yes/no): ").lower() != 'yes':
            break
    
    with open("customers.pkl", "wb") as f:
        pickle.dump(customers, f)

def write_items():
    items = []
    print('\n' * 2 + '$' * 52 + 'ITEMS' + '$' * 52)
    while True:
        num = int(input('Enter customer serial number: '))
        item_count = int(input("Enter the number of items: "))
        customer_items = []
        total = 0
        for _ in range(item_count):
            name = input('Enter the item: ')
            price = float(input('Enter the price of item: '))
            customer_items.append(Item(name, price))
            total += price
        items.append((num, customer_items))
        print(f"Total bill for customer {num}: ${total:.2f}")
        if input("Do you want to add items for more customers? (yes/no): ").lower() != 'yes':
            break
    
    with open("items.pkl", "wb") as f:
        pickle.dump(items, f)

def read_customers():
    try:
        with open("customers.pkl", "rb") as f:
            customers = pickle.load(f)
        for customer in customers:
            print(f"Serial: {customer.num}, Name: {customer.name}, Date: {customer.date}")
    except FileNotFoundError:
        print("No customer records found.")

def read_items():
    try:
        with open("items.pkl", "rb") as f:
            items = pickle.load(f)
        for num, customer_items in items:
            print(f"Customer {num}:")
            for item in customer_items:
                print(f"  Item: {item.name}, Price: ${item.price:.2f}")
    except FileNotFoundError:
        print("No item records found.")

def search_customer():
    try:
        with open("customers.pkl", "rb") as f:
            customers = pickle.load(f)
        search_num = int(input("Enter the serial number of the customer to search: "))
        for customer in customers:
            if customer.num == search_num:
                print(f"Name: {customer.name}, Date: {customer.date}")
                return
        print("Customer not found.")
    except FileNotFoundError:
        print("No customer records found.")

def append_customers():
    try:
        with open("customers.pkl", "rb") as f:
            customers = pickle.load(f)
    except FileNotFoundError:
        customers = []
    
    print('APPEND NEW CUSTOMERS:')
    while True:
        num = max([c.num for c in customers], default=0) + 1
        name = input("Enter the name of the customer: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        customers.append(Customer(num, name, date))
        if input("Do you want to add more records? (yes/no): ").lower() != 'yes':
            break
    
    with open("customers.pkl", "wb") as f:
        pickle.dump(customers, f)

def append_items():
    try:
        with open("items.pkl", "rb") as f:
            items = pickle.load(f)
    except FileNotFoundError:
        items = []
    
    print('APPEND ITEMS FOR NEW CUSTOMERS:')
    while True:
        num = int(input('Enter customer serial number: '))
        item_count = int(input("Enter the number of items: "))
        customer_items = []
        total = 0
        for _ in range(item_count):
            name = input('Enter the item: ')
            price = float(input('Enter the price of item: '))
            customer_items.append(Item(name, price))
            total += price
        items.append((num, customer_items))
        print(f"Total bill for customer {num}: ${total:.2f}")
        if input("Do you want to add items for more customers? (yes/no): ").lower() != 'yes':
            break
    
    with open("items.pkl", "wb") as f:
        pickle.dump(items, f)

def generate_bill():
    try:
        with open("customers.pkl", "rb") as f:
            customers = pickle.load(f)
        with open("items.pkl", "rb") as f:
            items = pickle.load(f)
    except FileNotFoundError:
        print("Customer or item data not found.")
        return

    customer_num = int(input("Enter the customer serial number to generate the bill: "))
    
    customer = next((c for c in customers if c.num == customer_num), None)
    if not customer:
        print("Customer not found.")
        return

    customer_items = next((item_list for num, item_list in items if num == customer_num), None)
    if not customer_items:
        print("No items found for this customer.")
        return

    print("\n" + "=" * 40)
    print(f"BILL FOR CUSTOMER: {customer.name}")
    print(f"Date: {customer.date}")
    print("=" * 40)
    print("Item Name".ljust(30) + "Price")
    print("-" * 40)
    
    total = 0
    for item in customer_items:
        print(f"{item.name.ljust(30)}${item.price:.2f}")
        total += item.price

    print("-" * 40)
    print(f"Total:".ljust(30) + f"${total:.2f}")
    print("=" * 40)

def collect_feedback():
    try:
        with open("feedback.pkl", "rb") as f:
            feedback_list = pickle.load(f)
    except FileNotFoundError:
        feedback_list = []

    print("CUSTOMER FEEDBACK")
    customer_num = int(input("Enter customer serial number: "))
    rating = int(input("Enter rating (1-5): "))
    comment = input("Enter feedback comment: ")

    feedback = Feedback(customer_num, rating, comment)
    feedback_list.append(feedback)

    with open("feedback.pkl", "wb") as f:
        pickle.dump(feedback_list, f)

    print("Feedback recorded successfully!")

def view_feedback():
    try:
        with open("feedback.pkl", "rb") as f:
            feedback_list = pickle.load(f)
        
        if not feedback_list:
            print("No feedback records found.")
            return

        print("\n" + "=" * 60)
        print("CUSTOMER FEEDBACK RECORDS")
        print("=" * 25)
        for feedback in feedback_list:
            print(f"Customer Number: {feedback.customer_num}")
            print(f"Rating: {feedback.rating}/5")
            print(f"Comment: {feedback.comment}")
            print(f"Date: {feedback.date}")
            print("-" * 60)
    except FileNotFoundError:
        print("No feedback records found.")

def main_menu():
    while True:
        print("$" * 25 + "||SUPERMARKET MANAGEMENT||" + "$" * 25)
        print('''WELCOME TO MAIN MENU OF OUR PAGE

        1. ADD NEW CUSTOMERS
        2. ADD ITEMS PURCHASED BY CUSTOMERS AND GET THE BILL
        3. REVIEW CUSTOMER DETAILS
        4. REVIEW ITEMS PURCHASED BY CUSTOMERS
        5. SEARCH FOR A CUSTOMER
        6. ADD NEW CUSTOMERS (APPEND)
        7. ADD ITEMS FOR NEW CUSTOMERS (APPEND)
        8. GENERATE BILL FOR A CUSTOMER
        9. COLLECT CUSTOMER FEEDBACK
        10. VIEW CUSTOMER FEEDBACK
        11. EXIT''')

        try:
            choice = int(input("ENTER YOUR CHOICE (1-11): "))
            if choice == 1:
                write_customers()
            elif choice == 2:
                write_items()
            elif choice == 3:
                read_customers()
            elif choice == 4:
                read_items()
            elif choice == 5:
                search_customer()
            elif choice == 6:
                append_customers()
            elif choice == 7:
                append_items()
            elif choice == 8:
                generate_bill()
            elif choice == 9:
                collect_feedback()
            elif choice == 10:
                view_feedback()
            elif choice == 11:
                print("Thank you for using the Supermarket Management System.")
                break
            else:
                print("Please enter a correct choice (1-11).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main_menu()
