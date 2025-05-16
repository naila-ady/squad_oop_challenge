from inventory import Inventory
from electronics import Electronics
from grocery import Grocery
from clothing import Clothing
from datetime import date
from exceptions import InventoryError

def main():
    inventory = Inventory()
    try:
        inventory.load_from_file("inventory.json")
        print("Inventory loaded successfully.\n")
    except Exception as e:
        print(f"Could not load inventory, starting fresh. Error: {e}\n")

    while True:
        print("\n--- Inventory Management System ---")
        print("1: Add Product")
        print("2: Search Product")
        print("3: Sell Product")
        print("4: Save Product")
        print("5: Load Product")
        print("6: View All Products")
        print("7: Exit")

        choice = input("Select One Option: ")

        if choice == "1":
            print("\nSelect Product Type:")
            print("1. Electronics")
            print("2. Grocery")
            print("3. Clothing")
            res = input("Enter choice (1-3): ")
            try:
                if res == "1":
                    prod_id = input("Product ID: ")
                    name = input("Name: ")
                    price = float(input("Price: "))
                    stck_qty = int(input("Quantity In Stock: "))
                    warranty = input("Warranty: ")
                    brand = input("Brand: ")

                    product = Electronics(prod_id, name, price, stck_qty, warranty, brand)
                    inventory.add_product(product)
                    print("Electronics product added!")

                elif res == "2":
                    prod_id = input("Product ID: ")
                    name = input("Name: ")
                    price = float(input("Price: "))
                    stck_qty = int(input("Quantity In Stock: "))
                    exp_year = int(input("Expiry year (YYYY): "))
                    exp_month = int(input("Expiry month (MM): "))
                    exp_day = int(input("Expiry day (DD): "))
                    expiry = date(exp_year, exp_month, exp_day)

                    product = Grocery(prod_id, name, price, stck_qty, expiry)
                    inventory.add_product(product)
                    print("Grocery item added!")

                elif res == "3":
                    prod_id = input("Product ID: ")
                    name = input("Name: ")
                    price = float(input("Price: "))
                    stck_qty = int(input("Quantity In Stock: "))
                    size = input("Size: ")
                    material = input("Material: ")

                    product = Clothing(prod_id, name, price, stck_qty, size, material)
                    inventory.add_product(product)
                    print("Clothing item added!")

                else:
                    print("Invalid product type choice.")
            except Exception as e:
                print(f"Error adding product: {e}")

        elif choice == "2":
            user_name = input("Enter name to search: ").strip().lower()
            results = inventory.search_by_name(user_name)

            if results:
                print("\nSearch Results:")
                for product in results:
                    print(product)
            else:
                print("No products found with that name.")


        elif choice == "3":
            product_id = input("Enter Product ID to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            try:
                inventory.sell_product(product_id, quantity)
                print("Product sold successfully!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            try:
                inventory.save_to_file("inventory.json")
                print("Inventory saved to 'inventory.json'.")
            except Exception as e:
                print(f"Error in saving: {e}")

        elif choice == "5":
            try:
                inventory.load_from_file("inventory.json")
                print("Products loaded successfully from 'inventory.json'.")
            except Exception as e:
                print(f"Error in loading: {e}")

        elif choice == "6":
            all_products = inventory.list_all_products()
            if all_products:
                print("\n--- Product List ---")
                for product in all_products:
                    print(product)
            else:
                print("No products in inventory.")

        elif choice == "7":
            try:
                inventory.save_to_file("inventory.json")
                print("Inventory saved. Exiting.")
            except Exception as e:
                print(f"Failed to save inventory: {e}")
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()


        
