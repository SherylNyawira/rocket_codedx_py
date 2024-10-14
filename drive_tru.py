# A list representing the menu at a fast-food drive-thru
menu = {
    1: '🍔 Cheeseburger',
    2: '🍟 Fries',
    3: '🥤 Soda',
    4: '🍦 Ice Cream',
    5: '🍪 Cookie'
}

# Function to display the welcome menu
def welcome():
    print("Welcome to the Fast-Food Drive-Thru! Here's our menu:")
    for item_num, item_name in menu.items():
        print(f"{item_num}. {item_name}")

# Function to get the item based on the item number
def get_item(item_number):
    return menu.get(item_number, "Sorry, that item number is not on our menu.")

# Main program function that takes user input
def main():
    welcome()  # Show the welcome menu
    try:
        order_number = int(input("Please enter the item number you'd like to order: "))
        print(f"You ordered: {get_item(order_number)}")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
