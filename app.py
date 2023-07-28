from flask import Flask, jsonify, request

app = Flask(__name__)

books = [{
    'id': 1,
    'title':'Diary of a Wimpy Kid',
    'author':'Jeff Kinney'
    },
    {
     'id': 2,
     'title':'Moby-Dick',
     'author':'Herman Melville'
    },
    {
    'id': 3,
    'title':'Harry Potter and the Philosofal Stone',
    'author':'J.K. Rowling'
    }
]

#CRUD with an API

#Get book by ID
@app.route('/books', methods=['GET'])
def get_book():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def obtain_book(id):
    for book in books:
       if book.get('id') == id:
          return jsonify(book)
       
#Update book by ID
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_id(id):
    alter_book = request.get_json()  #Request for Server
    for i, book in enumerate(books): #Returning ID and Book-name with the enumerate function;
        if book.get('id') == id:
            books[i].update(alter_book)
            return jsonify(books[i])

#Create new book
@app.route('/books',methods=['POST'])
def include_new_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)


#Delete existent book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    deleted_book = request.get_json()
    for i, book in enumerate(books):
        if book.get('id') == id:
            del books[i]
            
    return jsonify(books[i])

app.run(port=8000, host='localhost', debug=True)
