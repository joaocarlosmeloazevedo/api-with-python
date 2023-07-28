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

app.run(port=8000, host='localhost', debug=True)
