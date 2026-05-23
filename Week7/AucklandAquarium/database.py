import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect("aquarium.db")

        self.cursor = self.connection.cursor()

        self.create_table()

    # Create fish table
    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fish_inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fish_category TEXT,
                quantity INTEGER
            )
        """)

        self.connection.commit()

    # Add fish to database
    def add_fish(self, fish_category):

        # Check if fish already exists
        self.cursor.execute("""
            SELECT quantity FROM fish_inventory
            WHERE fish_category = ?
        """, (fish_category,))

        result = self.cursor.fetchone()

        # If fish exists, update quantity
        if result:

            quantity = result[0] + 1

            self.cursor.execute("""
                UPDATE fish_inventory
                SET quantity = ?
                WHERE fish_category = ?
            """, (quantity, fish_category))

        # Otherwise insert new fish
        else:

            self.cursor.execute("""
                INSERT INTO fish_inventory (fish_category, quantity)
                VALUES (?, ?)
            """, (fish_category, 1))

        self.connection.commit()

    # Display inventory
    def display_inventory(self):

        self.cursor.execute("""
            SELECT fish_category, quantity
            FROM fish_inventory
        """)

        records = self.cursor.fetchall()

        print("\n===== Aquarium Fish Inventory =====")

        for fish, quantity in records:

            print(f"Fish Category : {fish}")
            print(f"Number Available : {quantity}")
            print("-----------------------------")

    # Close database
    def close_connection(self):
        self.connection.close()