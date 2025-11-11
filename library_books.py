
all_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    },
    {
        "id": "B3",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": True,
        "due_date": None,
        "checkouts": 3
    },
    {
        "id": "B4",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True,
        "due_date": None,
        "checkouts": 4
    },
    {
        "id": "B5",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "available": True,
        "due_date": None,
        "checkouts": 6
    },
    {
        "id": "B6",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "available": False,
        "due_date": "2025-11-10",
        "checkouts": 8
    },
    {
        "id": "B7",
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "available": True,
        "due_date": None,
        "checkouts": 1
    },
    {
        "id": "B8",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-Age",
        "available": False,
        "due_date": "2025-11-12",
        "checkouts": 3
    }
# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
]
def view_all_books(all_books):
    print('Available Books:')
    for book in all_books:
            if (book["available"]== True):
                print(f"Book ID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print ()
[]
# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
[]
def search_all_books(all_books):
    search_term = input("Enter the author or genre of the book you would like to look up ").lower()
    matching_books = []
    for book in all_books:
        if search_term in book["author"].lower() or search_term in book["genre"].lower():
                matching_books.append(book)
    if matching_books:
        print("Matching Books:")
        for book in matching_books:
                print(f"Book ID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Genre: {book['genre']}")
                print ()
    else:
        print("No books found matching your search.")

view_all_books(all_books)
search_all_books(all_books)