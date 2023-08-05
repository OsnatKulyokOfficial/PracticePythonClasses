import datetime
import os


# Get the current working directory
# current_directory = os.getcwd()
# print("Current working directory:", current_directory)


# Print a message
# print("hello the first")

class LMS:
        """ 
        This class is used to keep records of the library's books.
        It has four modules: "Display Books", "Issue Books", "Return Books", "Add Book"
        """
        
        def __init__(self, list_of_books, library_name):
            self.list_of_books = list_of_books    # File containing the list ofbooks
            self.library_name = library_name           # Name of the library
            self.books_dict = {}                       # Dictionary to storebook details
            Id = 101
            with open(self.list_of_books) as bk:
                content = bk.readlines()
                for line in content:
                    self.books_dict.update({str(Id): {"books_title": line.replace("\n", ""), "lender_name": "", "Issue_data": "", "Status": "Available" }})
                    Id +=1
                    
        def __str__(self):
            book_titles = [book["books_title"] for book in self.books_dict.values()]
            return "\n".join(book_titles)
        
        def display_books(self):
            print("--------------------------------Lists of Books--------------------------------")
            print("Books ID", "\t", "Title")
            print("----------------------------------------------------------------")
            for key, value in self.books_dict.items():
                print(key, "\t\t", value.get("books_title"), "-[",value.get("Status"),"]")   
                
        
        def Issue_books(self):
            books_id = input("Enter Book ID: ")
            current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if books_id in self.books_dict.keys():
                if not self.books_dict[books_id]["Status"] == "Available":
                    print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} \ on {self.books_dict[books_id]['Issue_date']}")
                    return self.Issue_books()
                elif self.books_dict[books_id]['Status'] == 'Available':
                    your_name = ans = input("Please Enter Your Nmae: ")                
                    self.books_dict[books_id]['lender_name'] = your_name
                    self.books_dict[books_id]['Issue_date'] = current_date
                    self.books_dict[books_id]['Status'] = 'Already issued'
                    print('Book Issued Successfuliy!!! \n')
            else: 
                print('Book ID not !!!')              
                return self.Issue_books()
                
                
        def add_books(self):
            new_books = input("Enter book title: ")
            if new_books == "":
                return self.add_books
            elif len(new_books) > 25:
                print("Book title name is too long! Title length should be less then 25 chars.")
                return self.add_books 
            else: 
                with open(self.list_of_books, 'a') as bk:
                    bk.writelines(f"{new_books} \n")
                    self.books_dict.update({str(int(max(self.books_dict.keys())) + 1): {"books_title": new_books, "lender_name": "", "Issue_date": "", "Status": "Available"}})
                    print(f"This book `{new_books.title}` has been added successfully 😉")
            
        
        def return_books(self):
            books_id = input("Please enter book ID : ")
            if books_id in self.books_dict.keys():
                if self.books_dict[books_id]["Status"] == "Available":
                    print("This book is already available in library. Please check your book ID.")
                    return self.return_books()
                elif not self.books_dict[books_id]["Status"] == "Available":
                    self.books_dict[books_id]["lender_name"] = ""
                    self.books_dict[books_id]["Issue_date"] = ""
                    self.books_dict[books_id]["Status"] = "Available"
                    print("Successfully updated 😎 \n")
            else: 
                print("Book ID is not found 🙁")
                
            
try: 
    myLMS = LMS("list_of_books.txt", "Python's")
    press_key_list = {
        "D": "Display Books",
        "I": "Issue Books",
        "A": "Add Books",
        "R": "Return Books",
        "Q": "Quit"
    }
    Key_press = False
    while not (Key_press == "q"):
        print("\n" + "-" * 70)
        print(f"  Welcome To {myLMS.library_name} Library Management System  ")
        print("-" * 70 + "\n")

        print("Press the following keys to perform actions:\n")
        for key, value in press_key_list.items():
            print(f"- Press \"{key}\" to {value}.")

        print("\nPlease enter the corresponding key for the action you want to perform:")
        
        Key_press = input().lower()
        if Key_press == "i":
            print("\ncurrent selection : Issue Books\n")
            myLMS.Issue_books()
        elif Key_press == "a":
            print("\nCurrent selection : Add Book\n")
            myLMS.add_books()
        elif Key_press == "d":
            print("\nCurrent selection : Display Books\n")
            myLMS.display_books()
        elif Key_press == "r":
            print("\nCurrent selection : Return Book\n")
            myLMS.return_books()
        elif Key_press == "q":
            break
        else:
            continue

except Exception as e:
    print("Please check ur input, an error occurred:", str(e))

            
        
            
                
        
                
                
                
                        
# Create an instance of the LMS class
# print(LMS("List_of_books.txt", "Python's Library"))
# Create an instance of the LMS class
# lms_instance = LMS("List_of_Books.txt", "Python's Library")

# Call the display_books method
# lms_instance.display_books()
