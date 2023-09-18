from fastapi import FastAPI, Body

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

#list of book
books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get('/books')
async def first():
    return books

@app.get('/books/{book_title}')
async def get_book(book_title: str):
    for book in books:
        title = book.get('title')
        if title and title.casefold() == book_title.casefold():
            return book

@app.get('/books/')
def get_book_by_category(category: str):
    books_list = []
    for book in books:
        if book.get('category').casefold() == category.casefold():
            books_list.append(book)
        return books_list

@app.get('/books/{book_author}')
def get_book_by_category(book_author: str ,category: str):
    books_list = []
    for book in books:
        if book.get('Author').casefold() == book_author.casefold() \
                and book.get('category').casefold() == category.casefold():
            books_list.append(book)
        return books_list

@app.post('/books/create_book')
def create_book(new_book=Body()):
    try:
        books.append(new_book)
        return {'meessage': 'done'}
    except:
        return {'message': 'no'}

@app.put('/books/update_book')
def update_book(updated_book=Body()):
    for i in range (len(books)):
        if books[i].get('title').casefold() == updated_book.get('title').casefold():
            books[i] = updated_book

@app.delete('/books/delete_book/{book_title}')
def delete_book(book_title: str):
    for i in range (len(books)):
        if books[i].get('title').casefold() == book_title.casefold():
            books.pop(i)
            break

@app.get('/books/author/')
def get_books_by_author(author: str):
    books_list = []
    for book in books:
        if book.get('Author').casefold() == author.casefold():
            books_list.append(book)
    return books_list