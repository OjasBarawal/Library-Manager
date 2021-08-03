# Main App -- Storing Books in the Database + Type Hinting + SQLite3

from utils import database

USER_CHOICE = """
Enter following for : 
- 'a' to ADD a New Book.
- 'l' to LIST all the Books.
- 'r' to MARK a Book as Read.
- 'd' to DELETE a Book.
- 'q' to QUIT the App.
Your Choice : """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown Command. Please Try Again..!!')

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter the Name of the Book : ')
    author = input('Enter the Name of the Author : ')
    database.add_book(name, author)
    print('--> Book Added Successfully..!')


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f'{book["name"]} by {book["author"]} and read: {read}')
        print('----------------------------------')


def prompt_read_book():
    name = input('Enter the Name of the Book, you\'ve just finish Reading :  ')
    database.mark_book_as_read(name)
    print(f'--> \"{name}\" Marked as Read')


def prompt_delete_book():
    name = input('Enter the Book Name, you wish to Delete : ')
    database.delete_book(name)
    print('--> Book has been deleted successfully..!')


menu()
