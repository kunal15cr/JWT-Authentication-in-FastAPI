from passlib.context import CryptContext

paw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_user_db = {
    "johndoe": {
       "username": "johndoe",
         "hashed_password": paw_context.hash("secret")
         }
}

def get_user(username: str):
    user = fake_user_db.get(username)
    return user

def verify_password(plain_password: str, hashed_password: str):
    return paw_context.verify(plain_password, hashed_password)