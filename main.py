# Inventory System class
class InventorySystem:
    def __init__(self):
        self.inventory = {}  # Dictionary to store item details

    # Function to add new item
    def add_item(self):
        item_name = input("Enter the item name: ")
        if item_name in self.inventory:
            print(f"{item_name} already exists. Try updating the quantity instead.")
            return

        quantity = int(input(f"Enter quantity for {item_name}: "))
        price = float(input(f"Enter price for {item_name}: "))
        
        # Adding item to the inventory
        self.inventory[item_name] = {
            'quantity': quantity,
            'price': price
        }
        print(f"{item_name} added successfully!")

    # Function to update item quantity
    def update_quantity(self):
        item_name = input("Enter the item name to update: ")
        if item_name in self.inventory:
            new_quantity = int(input(f"Enter new quantity for {item_name}: "))
            self.inventory[item_name]['quantity'] = new_quantity
            print(f"{item_name}'s quantity updated to {new_quantity}.")
        else:
            print(f"{item_name} not found in the inventory.")

    # Function to remove an item
    def remove_item(self):
        item_name = input("Enter the item name to remove: ")
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"{item_name} removed successfully!")
        else:
            print(f"{item_name} not found in the inventory.")

    # Function to view the inventory
    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\n--- Inventory ---")
            for item, details in self.inventory.items():
                print(f"Item: {item}, Quantity: {details['quantity']}, Price: {details['price']}")
            print("----------------")

    # Main menu for the system
    def menu(self):
        while True:
            print("\nInventory Management System")
            print("1. Add Item")
            print("2. Update Quantity")
            print("3. Remove Item")
            print("4. View Inventory")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.update_quantity()
            elif choice == '3':
                self.remove_item()
            elif choice == '4':
                self.view_inventory()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice! Please try again.")

# Main function to run the system
if __name__ == "__main__":
    system = InventorySystem()
    system.menu()
