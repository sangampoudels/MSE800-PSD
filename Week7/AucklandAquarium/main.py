from factory import FishFactory
from database import Database


def main():

    db = Database()

    print("=== Auckland Aquarium Management System ===")

    while True:

        print("\nChoose an option:")
        print("1. Add Fish")
        print("2. Display Inventory")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # Add fish
        if choice == "1":

            print("\nAvailable Fish Categories:")
            print("Goldfish")
            print("Shark")
            print("Angelfish")
            print("Tuna")
            print("Salmon")

            fish_name = input("\nEnter fish name: ")

            fish = FishFactory.create_fish(fish_name)

            if fish:

                db.add_fish(fish.get_category())

                print(f"{fish.get_category()} added successfully.")

            else:
                print("Invalid fish type!")

        # Display inventory
        elif choice == "2":

            db.display_inventory()

        # Exit
        elif choice == "3":

            print("\nExiting Aquarium Management System...")
            break

        else:
            print("Invalid option!")

    db.close_connection()

    print("\nThank you for using the system.")


if __name__ == "__main__":
    main()