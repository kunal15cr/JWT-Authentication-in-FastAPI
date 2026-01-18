from passlib.context import CryptContext

# IMPORTANT: truncate_error REMOVED
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def normalize_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    return password_bytes.decode("utf-8", errors="ignore")


fake_user_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": pwd_context.hash(
            normalize_password("Kunal#15cr")
        ),
    }
}


def get_user(username: str):
    return fake_user_db.get(username)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password = normalize_password(plain_password)
    return pwd_context.verify(plain_password, hashed_password)
