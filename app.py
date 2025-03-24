from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

import logging

from user_model import Base, User
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

order_number = 0

app = Flask(__name__)
app.secret_key = "this is a secret key"

engine = create_engine("sqlite:///users.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

def set_password(self, password):
    self.password = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password, password)


@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    hashed_password = generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    session.add(new_user)
    session.commit()
    return jsonify({'message': 'User created'}), 201

# @app.route('/create_account', methods=['POST'])
# def create_account():
#     data = request.get_json()

#     # Extract form data
#     name = data['name']
#     email = data['email']
#     password = data['password']


#     new_user = User(
#         name=name,
#         email=email,
#         password=password
#     )


#     print("we've made new user, and have not entered try block")
#     try:
#         session.add(new_user)
#         session.commit()
#         return jsonify({'message': 'Account created successfully'}), 201

#     except Exception as e:
#         session.rollback()  # Rollback the transaction
#         app.logger.error(f"Error during commit: {e}")
#         return 'There was an issue adding your task'





if __name__ == '__main__':
    app.run(debug=True)
