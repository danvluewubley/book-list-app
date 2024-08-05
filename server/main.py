from flask import Flask, jsonify, request
from models import db, User
from flask_cors import CORS
from werkzeug.security import generate_password_hash
from config import app, db


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

    return jsonify({"message": "User created successfully"}), 201

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


@app.route("/api/books", methods=['GET'])
def books():
  return jsonify({"books": ["Harry Potter", "Percy Jackson"]})

if __name__ == "__main__":
  app.run(debug=True, port=8080)