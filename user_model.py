from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # Rename table to 'users' as this is what the model represents.

    # Define the columns corresponding to the 'CreateAccount' form fields
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False)  # Ensure email is unique unique=True
    password = Column("password", String, nullable=False)

    def tojson(self):
        # Convert the User object to JSON format
        new_json_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
        return new_json_dict