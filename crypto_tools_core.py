import base64
import hashlib
import secrets
from argon2 import PasswordHasher

#* crypto_tools_core.py
#? File contains cryptographic functions that process API requests data

async def hash_generate_SHA256(input_str: str) -> str:
    """
    Generate SHA-256 hash for the input string
    """
    hashed_string = hashlib.sha256(input_str.encode())

    return hashed_string.hexdigest()


async def hash_generate_SHA512(input_str: str) -> str:
    """
    Generate SHA-512 hash for the input string
    """
    hashed_string = hashlib.sha512(input_str.encode())

    return hashed_string.hexdigest()


async def hash_generate_argon2(input_str: str, input_salt: str) -> str:
    """
    Generate Argon2 hash for the input string
    """    
    ph = PasswordHasher()
    hashed_string = ph.hash(input_str, salt=input_salt.encode())

    return hashed_string


async def random_int_number_generate(min_int: int, max_int: int) -> int:
    """
    Generate random integer number from the specified range of integers [min, max]
    """
    rng = secrets.SystemRandom()
    random_integer_number = rng.randint(min_int, max_int)

    return random_integer_number


async def random_string_generate(length: int) -> str:
    """
    Generate random string of a given length
    """
    symbols = 'abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+|~`[];:'
    random_string = ''.join(secrets.choice(symbols) for i in range(length))

    return random_string


async def base64_encode(input_str: str) -> str:
    """
    Encode input string with base64 and return encoded string (as string)
    """
    encoded_string = base64.b64encode(input_str.encode())

    return encoded_string.decode()


async def base64_decode(input_str: str) -> str:
    """
    Decode base64-encoded input string and return decoded string (as string)
    """
    decoded_string = base64.b64decode(input_str)

    return decoded_string.decode()