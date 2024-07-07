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
            item_add = input("Enter the item you want to add: ").strip()
            shopping_list.append(item_add)
            print(f"{item_add} has been added to the shopping list.")

        elif choice == '2':
            item_remove = input("Enter the item you want to remove: ").strip()
            if item_remove in shopping_list:
                shopping_list.remove(item_remove)
                print(f"{item_remove} has been removed from the shopping list.")
            else:
                print(f"{item_remove} is not in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
