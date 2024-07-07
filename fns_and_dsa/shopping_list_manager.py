def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_add = input("Enter the item you wanna add: ")
            shopping_list.append(item_add)

        elif choice == '2':
            item_remove = input("Remove an item: ")
            if item_remove in shopping_list:
                shopping_list.remove(item_remove)
            print(f"This item {item_remove} is not in the shopping list")

        elif choice == '3':
            for item in shopping_list:
                print(f"- {item}")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()