from connect import connect
import csv


# Create table
def CreateTable():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20),
        UNIQUE(name, phone)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()


# Add contact manually
def AddContact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
        ON CONFLICT (name, phone) DO NOTHING
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()


# Input contact from console
def AddContactFromInput():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    AddContact(name, phone)


# Import from CSV (NO duplicates)
def ImportFromCsv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) != 2:
                continue

            name, phone = row

            cur.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (name, phone) DO NOTHING
            """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()


# Show all contacts
def GetAll():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    if not rows:
        print("No data")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

    cur.close()
    conn.close()


# Update phone
def UpdateContact(name, new_phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()


# Search by name
def SearchByName(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        ('%' + name + '%',)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Delete contact
def DeleteContact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name = %s OR phone = %s",
        (value, value)
    )

    conn.commit()
    cur.close()
    conn.close()


# MAIN MENU
if __name__ == "__main__":
    CreateTable()

    while True:
        print("\n1 - Import CSV")
        print("2 - Add contact")
        print("3 - Show all")
        print("4 - Update phone")
        print("5 - Search by name")
        print("6 - Delete contact")
        print("0 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            filename = input("Write file name: ")
            ImportFromCsv(filename)

        elif choice == "2":
            AddContactFromInput()

        elif choice == "3":
            GetAll()

        elif choice == "4":
            name = input("Name: ")
            phone = input("New phone: ")
            UpdateContact(name, phone)

        elif choice == "5":
            name = input("Search name: ")
            SearchByName(name)

        elif choice == "6":
            val = input("Enter name or phone: ")
            DeleteContact(val)

        elif choice == "0":
            break

        else:
            print("Invalid choice")