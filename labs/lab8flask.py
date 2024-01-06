# GET /books: Retrieves a list of books.
# GET /books/<id>: Retrieves a book by its ID.
# POST /books: Creates a new book.
# PUT /books/<id>: Updates an existing book by its ID.
# DELETE /books/<id>: Deletes a book by its ID.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data store
books = [
    {"id": 1, "title": "Book One", "author": "Author A"},
    {"id": 2, "title": "Book Two", "author": "Author B"}
]

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return jsonify(book) if book else ('', 404)


@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    new_book['id'] = len(books) + 1  # Simple ID assignment
    books.append(new_book)
    return jsonify(new_book), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return '', 404
    book_data = request.json
    book.update(book_data)
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)


# Testing in Bash
# Retrieve All Books: curl http://localhost:5000/books
# Retrieve a Specific Book by ID: curl http://localhost:5000/books/[ID]
# Create a New Book: curl -X POST -H "Content-Type: application/json" -d '{"title":"Example Book", "author":"Author Name"}' http://localhost:5000/books
# Update a Book: curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Title", "author":"Updated Author"}' http://localhost:5000/books/[ID]
# Delete a Book: curl -X DELETE http://localhost:5000/books/[ID]
    
# Testing in Windows Power Shell
# Retrieve All Books: Invoke-WebRequest -Uri http://localhost:5000/books -Method Get
# Retrieve a Specific Book by ID: Invoke-WebRequest -Uri http://localhost:5000/books/[ID] -Method Get
# Create a New Book: Invoke-WebRequest -Uri http://localhost:5000/books -Method Post -ContentType "application/json" -Body '{"title":"New Book", "author":"Author X"}'
# Update a Book: Invoke-WebRequest -Uri http://localhost:5000/books/[ID] -Method Put -ContentType "application/json" -Body '{"title":"Updated Title", "author":"Updated Author"}'
# Delete a Book: Invoke-WebRequest -Uri http://localhost:5000/books/[ID] -Method Delete

