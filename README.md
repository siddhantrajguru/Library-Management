# 📚 Library Book Management System

A simple command-line library management system built in Python that allows you to manage books, track issued books, and calculate fines for overdue returns.

## ✨ Features

- **📖 Add Books**: Add new books to the library with unique Book IDs
- **🗑️ Remove Books**: Remove books from the library system
- **📤 Issue Books**: Issue books to students with automatic due date calculation (14 days)
- **📥 Return Books**: Process book returns with automatic fine calculation
- **👀 View Books**: Display all books with their availability status
- **💾 Data Persistence**: All data is stored in JSON format for persistence across sessions

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

## 🚀 Installation

1. Clone this repository or download the Python file
2. Run the program using Python 3.6 or higher

## 💻 Usage

When you run the program, you'll see a menu with 6 options for managing your library books.

### 📖 Adding a Book
- Select option 1
- Enter a unique Book ID
- Enter the book title
- The book will be added to the library

### 🗑️ Removing a Book
- Select option 2
- Enter the Book ID of the book you want to remove
- The book will be removed from the system

### 📤 Issuing a Book
- Select option 3
- Enter the Book ID of the book to issue
- Enter the student's name
- The book will be marked as issued with a 14-day due date

### 📥 Returning a Book
- Select option 4
- Enter the Book ID of the book being returned
- The system will calculate any applicable fine (₹2 per day for overdue books)
- The book will be marked as available

### 👀 Viewing All Books
- Select option 5
- View all books in the library with their current status (Available/Issued)

## 💾 Data Storage

The system uses a JSON file (library_data.json) to store all data with books and issued book information structured in a hierarchical format.

## 💰 Fine Calculation

- Books have a 14-day borrowing period
- Fine is calculated at ₹2 per day for overdue books
- Fine is automatically calculated when returning books

## 💡 Example Usage

The system provides a simple menu-driven interface where you select options by entering numbers 1-6. For example, to add a book you would select option 1, enter a unique Book ID and title. To issue a book, select option 3, provide the Book ID and student name, and the system automatically sets a 14-day due date.

## 📁 File Structure

```
library-management-system/
│
├── library_management.py    # Main program file
├── library_data.json       # Data storage file (created automatically)
└── README.md              # This file
```

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## 🚀 Future Enhancements

- Add search functionality for books
- Implement user authentication
- Add book categories and authors
- Generate reports for issued books
- Add GUI interface
- Implement database storage instead of JSON

## 💬 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the author.
