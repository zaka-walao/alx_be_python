class Book:
    def __init__(self, title, author, year):
        """
        Constructor for Book class.
        
        :param title: str - The title of the book.
        :param author: str - The author of the book.
        :param year: int - The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to handle the deletion of a Book instance.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance in a human-readable form.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the Book instance that could recreate the book.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

