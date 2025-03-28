from repositories.db import get_pool
from werkzeug.security import generate_password_hash, check_password_hash


def signup_user(username: str, password: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            # Check if the user already exists
            cur.execute('SELECT id FROM users WHERE name = %s', (username,))
            if cur.fetchone():
                return False, 'Username already exists.'

            # Insert the new user into the database
            password_hash = generate_password_hash(password)

            cur.execute('INSERT INTO Users (name, password) VALUES (%s, %s)',
                        (username, password_hash))
            conn.commit()
            return True, 'Registration successful, please login.'
        
        
def login_user(username: str, password: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM users WHERE name = %s', (username,))
            user_record = cur.fetchone()
            if user_record:
                id, name, password_hash = user_record
                if check_password_hash(password_hash, password):
                    return True, id, name
            return False, None, 'Invalid username or password'