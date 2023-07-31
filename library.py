import sqlite3

# Step 2: Design the Database
def create_tables():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        book_id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        is_available INTEGER DEFAULT 1
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS borrowings (
                        borrowing_id INTEGER PRIMARY KEY,
                        book_id INTEGER NOT NULL,
                        borrower_name TEXT NOT NULL,
                        borrow_date TEXT NOT NULL,
                        due_date TEXT NOT NULL,
                        returned INTEGER DEFAULT 0,
                        FOREIGN KEY (book_id) REFERENCES books (book_id)
                    )''')

    conn.commit()
    conn.close()

# Step 3: Implement Library Functions
def add_book(title, author):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))

        conn.commit()
        conn.close()
        print("Book added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def borrow_book(book_id, borrower_name, borrow_date, due_date):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        # Check if the book is available before borrowing
        cursor.execute('SELECT is_available FROM books WHERE book_id=?', (book_id,))
        result = cursor.fetchone()

        if not result:
            print(f"Book with ID {book_id} does not exist in the database.")
        elif result[0] == 0:
            print("Book is not available for borrowing.")
        else:
            # Update book availability status to 0 (not available)
            cursor.execute('UPDATE books SET is_available=0 WHERE book_id=?', (book_id,))
            
            # Add borrowing information to the borrowings table
            cursor.execute('INSERT INTO borrowings (book_id, borrower_name, borrow_date, due_date) VALUES (?, ?, ?, ?)',
                           (book_id, borrower_name, borrow_date, due_date))
            print("Book borrowed successfully!")

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def view_books():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()

        conn.close()
        return books
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def view_borrowed_books():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM borrowings WHERE returned=0')
        borrowed_books = cursor.fetchall()

        conn.close()
        return borrowed_books
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def mark_book_returned(borrowing_id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        # Update book return status to 1 (returned)
        cursor.execute('UPDATE borrowings SET returned=1 WHERE borrowing_id=?', (borrowing_id,))

        # Update book availability status to 1 (available)
        cursor.execute('SELECT book_id FROM borrowings WHERE borrowing_id=?', (borrowing_id,))
        book_id = cursor.fetchone()[0]
        cursor.execute('UPDATE books SET is_available=1 WHERE book_id=?', (book_id,))

        conn.commit()
        conn.close()
        print("Book marked as returned.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 4: User Interface
def main():
    create_tables()

    while True:
        print("Choose an option:")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. View all books")
        print("4. View borrowed books")
        print("5. Mark a book as returned")
        print("0. Exit")

        choice = int(input())

        if choice == 1:
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            add_book(title, author)
        elif choice == 2:
            book_id = int(input("Enter the book ID: "))
            borrower_name = input("Enter your name: ")
            borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            borrow_book(book_id, borrower_name, borrow_date, due_date)
        elif choice == 3:
            books = view_books()
            for book in books:
                print(book)
        elif choice == 4:
            borrowed_books = view_borrowed_books()
            for book in borrowed_books:
                print(book)
        elif choice == 5:
            borrowing_id = int(input("Enter the borrowing ID of the book to mark as returned: "))
            mark_book_returned(borrowing_id)
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
