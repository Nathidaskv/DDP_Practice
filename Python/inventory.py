# Add comment
# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {
    "Product A" : 100, 
    "Product B" : 150, 
    "Product C" : 200, 
    "Product D" : 250, 
    "Product E" :300
    }

# Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    if item in inventory:
        # 2. If it does, increase its quantity.
        inventory[item] =  inventory[item] + quantity #inventory[item] += quantity >>>you can write this way
    # 3. If not, add the item to the inventory with the given quantity.
    else : 
        inventory[item] = quantity #if we access the key which is not in the dict. it will add new item in the dict
    return inventory



# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    for item, qualtity in inventory.item()

    print(inventory)
    # 2. Print each item's name and its quantity.



# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
    pass

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")
        
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        if choice == "1":
            item_name = input("Item name: ")
            item_quantity = int(input("Quantity: "))
        #    and then call the add_item function.
            print(add_item(item_name, item_quantity))

        # 2. If the choice is '2', call the view_inventory function.   
        elif choice == "2":
            view_inventory()

        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        elif choice == "3":
        #    and then call the update_item function.
            update_item()
        
        # 4. If the choice is '4', break the loop to exit the program.       
        elif choice == "4":
            break
        




        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 5. For any other input, display an error message.
        pass

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()


"""
Error >> code is not running

Exception 
    >> example users fill in the invalid input
    >> excaption handling : try & except
"""
