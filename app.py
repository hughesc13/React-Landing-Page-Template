from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS


#to run:
#flask run

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # You can use any database like PostgreSQL, MySQL, etc.
# db = SQLAlchemy(app)
# CORS(app)  # To handle CORS issues when connecting from React frontend


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



@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()

    # Extract form data
    name = data['name']
    email = data['email']
    password = data['password']
    dietary_preferences = data.get('dietaryPreferences', '')
    allergies = data.get('allergies', '')

    # Check if email already exists
    # existing_user = session.query(User).filter_by(email=email).first()
    # if existing_user:
    #     return jsonify({'error': 'Email already exists'}), 400

    # Create a new user object
    new_user = User(
        name=name,
        email=email,
        password=password,
        dietary_preferences=dietary_preferences,
        allergies=allergies
    )
    print("we've made new user, and have not entered try block")
    try:
        session.add(new_user)
        session.commit()
        return jsonify({'message': 'Account created successfully'}), 201

    except Exception as e:
        session.rollback()  # Rollback the transaction
        app.logger.error(f"Error during commit: {e}")
        return 'There was an issue adding your task'

    



# # Define the route to handle account creation
# @app.route('/createaccount', methods=['POST'])
# def create_account():
#     data = request.get_json()  # Get the JSON data sent from the frontend
    
#     # Extract values from the request
#     name = data['name']
#     email = data['email']
#     password = data['password']
#     dietary_preferences = data.get('dietaryPreferences', '')
#     allergies = data.get('allergies', '')
    
#     # Check if the email already exists
#     existing_user = User.query.filter_by(email=email).first()
#     if existing_user:
#         return jsonify({'error': 'Email already exists'}), 400

#     # Create a new user
#     new_user = User(
#         name=name,
#         email=email,
#         password=password,  # You should hash the password before storing it in production
#         dietary_preferences=dietary_preferences,
#         allergies=allergies
#     )

#     # Add the user to the database
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'Account created successfully'}), 201

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
