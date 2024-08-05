from flask import Flask, jsonify, request
from models import db, User
from flask_cors import CORS
from werkzeug.security import generate_password_hash

def create_app():
  app = Flask(__name__)
  CORS(app, supports_credentials=True)
  app.config['SECRET_KEY'] = 'cwhi3oh8'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
  db.init_app(app)

  with app.app_context():
      db.create_all()

  return app

app = create_app()

@app.route('/')
def index():
  return "<p>Hello</p>"


@app.route('/signup', methods=['POST'])
def signup():
  data = request.get_json()

  email = data.get('email')
  password = data.get('password')

  if not email or not password:
      return jsonify({"error": "Email and password are required"}), 400

  hashed_password = generate_password_hash(password, method="pbkdf2")

  new_user = User(email=email, password=hashed_password)
  db.session.add(new_user)
  db.session.commit()

  return jsonify({"message": "User created successfully"}), 201


@app.route("/api/books", methods=['GET'])
def books():
  return jsonify({"books": ["Harry Potter", "Percy Jackson"]})

if __name__ == "__main__":
  app.run(debug=True, port=8080)