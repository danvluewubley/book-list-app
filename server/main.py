from flask import jsonify, request, redirect
from models import db, User, Books
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from __init__ import create_app

app = create_app()

@app.route('/')
def index():
  return "<p>Hello</p>"


@app.route('/users', methods=['GET'])
def users():
  user_list = User.query.all()
  result = [user.to_json() for user in user_list]
  return jsonify(result)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(password, method="pbkdf2")

    new_user = User(email=email, password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating user"}), 500

    login_user(new_user)
    return jsonify({"message": "User created successfully"}), 201

@app.route('/login', methods=["POST"])
def login():    
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password): 
        return jsonify({"success": False}), 401

    login_user(user)
    return jsonify({"success": True}), 200  


@app.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return redirect("/")


@app.route('/delete/<int:id>', methods=["DELETE"])
def delete_user(id):
  try:
    user = User.query.get(id)
    if user is None:
      return jsonify({'error':'user not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message':'user deleted'}), 200
  except Exception as e:
    return jsonify({"error":str(e)}), 500

@app.route('/update/<int:id>', methods=["PATCH"])
def update_user(id):
  try:
    user = User.query.get(id)
    if user is None:
      return jsonify({'error':'user not found'}), 404
    
    data = request.get_json()

    user.email = data.get('email',user.email)
    user.password = data.get('password',user.password)

    db.session.commit()
    return jsonify(user.to_json()), 200
  except Exception as e:
    return jsonify({"error":str(e)}), 500

with app.app_context():
  db.create_all()

@app.route('/books', methods=['GET'])
def books():
  book_list = Books.query.all()
  result = [book.to_json() for book in book_list]
  return jsonify(result)

@app.route('/book/add', methods=['POST'])
def add_book():
    data = request.get_json()

    title = data.get('title').strip()
    author = data.get('author')
    genre = data.get('genre')
    user_id = data.get('user_id')

    existing_book = Books.query.filter(db.func.lower(Books.title) == db.func.lower(title)).first()
    if existing_book:
        return jsonify({"error": "Book already exists"}), 400

    new_book = Books(title=title, author=author, genre=genre, user_id=user_id)
    try:
        db.session.add(new_book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error adding book"}), 500

    return jsonify({"message": "Book added successfully"}), 201


@app.route('/book/delete/<int:id>', methods=["DELETE"])
def delete_book(id):
  try:
    book = Books.query.get(id)
    if book is None:
      return jsonify({'error':'book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message':'book deleted'}), 200
  except Exception as e:
    return jsonify({"error":str(e)}), 500

@app.route('/book/update/<int:id>', methods=["PATCH"])
def update_book(id):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    try:
        book = Books.query.get(id)
        if book is None:
            return jsonify({'error': 'book not found'}), 404
        
        data = request.get_json()

        if 'user_id' in data:
            book.user_id = data['user_id']
        if 'title' in data:
            book.title = data['title']
        if 'author' in data:
            book.author = data['author']
        if 'genre' in data:
            book.genre = data['genre']

        db.session.commit()
        return jsonify(book.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating book"}), 500
    
  
with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(debug=True, port=8080)