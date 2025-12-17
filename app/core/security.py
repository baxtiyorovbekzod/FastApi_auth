import secrets

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




def hash_password(plain_password: str) -> str:
    ok = plain_password[:72]  
    return pwd_context.hash(ok)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain-text password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def generate_token():
    return secrets.token_urlsafe(48)