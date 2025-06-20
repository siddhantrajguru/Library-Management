
import json
import os
from datetime import datetime, timedelta

DATA_FILE = "library_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"books": {}, "issued": {}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_book(data):
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    if book_id in data["books"]:
        print("Book ID already exists.")
        return
    data["books"][book_id] = {"title": title, "available": True}
    save_data(data)
    print("Book added successfully.")

def remove_book(data):
    book_id = input("Enter Book ID to remove: ")
    if book_id in data["books"]:
        del data["books"][book_id]
        data["issued"].pop(book_id, None)
        save_data(data)
        print("Book removed.")
    else:
        print("Book not found.")

def issue_book(data):
    book_id = input("Enter Book ID to issue: ")
    student_name = input("Enter Student Name: ")
    if book_id in data["books"] and data["books"][book_id]["available"]:
        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=14)
        data["books"][book_id]["available"] = False
        data["issued"][book_id] = {
            "student": student_name,
            "issue_date": issue_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d")
        }
        save_data(data)
        print(f"Book issued to {student_name}. Due on {due_date.date()}.")
    else:
        print("Book not available or not found.")

def return_book(data):
    book_id = input("Enter Book ID to return: ")
    if book_id in data["issued"]:
        return_date = datetime.now()
        due_date = datetime.strptime(data["issued"][book_id]["due_date"], "%Y-%m-%d")
        delta = (return_date - due_date).days
        fine = 0
        if delta > 0:
            fine = delta * 2  # ₹2 per day fine
        data["books"][book_id]["available"] = True
        del data["issued"][book_id]
        save_data(data)
        print(f"Book returned. Fine: ₹{fine}")
    else:
        print("Book was not issued.")

def show_books(data):
    print("\nAvailable Books:")
    for book_id, info in data["books"].items():
        status = "Available" if info["available"] else "Issued"
        print(f"ID: {book_id}, Title: {info['title']}, Status: {status}")

def main():
    data = load_data()
    while True:
        print("\n=== Library Book Management ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(data)
        elif choice == '2':
            remove_book(data)
        elif choice == '3':
            issue_book(data)
        elif choice == '4':
            return_book(data)
        elif choice == '5':
            show_books(data)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
