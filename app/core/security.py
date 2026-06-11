import bcrypt
from app.core.config import settings

def hash_password(password: str) -> str:
    """Genera un hash bcrypt para una contraseña."""
    salt = bcrypt.gensalt(rounds=12)  # Usamos 12 rondas por defecto
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si una contraseña coincide con su hash."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))