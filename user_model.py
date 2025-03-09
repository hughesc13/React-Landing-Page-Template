from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # Rename table to 'users' as this is what the model represents.

    # Define the columns corresponding to the 'CreateAccount' form fields
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)  # Ensure email is unique
    password = Column("password", String, nullable=False)
    dietary_preferences = Column("dietary_preferences", String, nullable=True)  # Optional field
    allergies = Column("allergies", String, nullable=True)  # Optional field

    def tojson(self):
        # Convert the User object to JSON format
        new_json_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "dietary_preferences": self.dietary_preferences,
            "allergies": self.allergies
        }
        return new_json_dict
