"""Auth Module"""
from jose import jwt


def encode_jwt(code: int) -> str:
    """
    Encode the int code into a JWT Token
    :param code:
    :return str:
    """
    return jwt.encode({'code': code}, 'secret', algorithm='HS256')


def decode_jwt(token: str) -> dict:
    """
    Decode a JWT Token and getting the dict payload.
    :param token:
    :return dict:
    """
    return jwt.decode(token, 'secret', algorithms=['HS256'])
