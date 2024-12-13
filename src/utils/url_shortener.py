import hashlib
import secrets

from pydantic import AnyUrl


def generate_short_code(url: AnyUrl, length: int = 6) -> str:
    salt = secrets.token_hex(8)
    print(url.__str__())
    hash_object = hashlib.md5((str(url) + salt).encode())
    short_code = hash_object.hexdigest()[:length]
    return short_code
