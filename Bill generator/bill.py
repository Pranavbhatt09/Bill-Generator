import os
import datetime

# Create a directory for generated bills if it doesn't exist
if not os.path.exists("final-amount"):
    os.makedirs("final-amount")

def generate_bill():
    current_time = datetime.datetime.now()
    bill_filename = current_time.strftime("%m-%d-%Y_%H-%M-%S") + ".txt"

    # Get order details from the user
    print("Enter the details of the items (Enter 'exit' to finish):")
    items = []
    total_price = 0.0
    while True:
        item_name = input("Item name: ")
        if item_name.lower() == 'exit':
            break
        try:
            item_price = float(input("Item_Amount: "))
            total_price += item_price
            items.append(f"{item_name}: ₹{item_price:.2f}")
        except ValueError:
            print("Invalid price. Please enter a valid number.")

    # Create the bill content
    bill_items = f"Bill Date / Time: {current_time}\n"
    bill_items += "\n".join(items)
    bill_items += f"\nTotal Price: ₹{total_price:.2f}"

    # Print the bill
    print("\n--- Bill ---")
    print(bill_items)

    # Save the bill to a file
    with open(os.path.join("final-amount", bill_filename), "w") as bill_file:
        bill_file.write(bill_items)

    print(f"Bill saved as {bill_filename} in final-amount directory.")

def print_bill():
    date_time_input = input("Enter the date and time of the bill (MM-DD-YYYY_hh-mm-ss): ")
    bill_filename = date_time_input + ".txt"

    try:
        with open(os.path.join("final-amount", bill_filename), "r") as bill_file:
            bill_data = bill_file.read()
            print("\nBill Data:")
            print(bill_data)
    except FileNotFoundError:
        print(f"Bill for {date_time_input} not found.")

if __name__ == "__main__":
    while True:
        print("\nBill Generator Menu:")
        print("1. Generate a new bill")
        print("2. Show existing bill")
        print("3. End")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            generate_bill()
        elif choice == '2':
            print_bill()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
