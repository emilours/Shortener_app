import secrets
import string
from fastapi import HTTPException, Request
import validators
import httpx
from sqlalchemy.orm import Session
from . import crud

def create_random_key(length: int = 5) -> str:
    """ Generate a random alphanumeric key of a given length """
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_random_key(db: Session) -> str:
    """ Generate a unique random key that is not already in the database """
    key = create_random_key()
    while crud.get_db_url_by_key(db, key):
        key = create_random_key()
    return key

def raise_bad_requests(message: str):
    """ Raise a 400 Bad Request """
    raise HTTPException(status_code=400, detail=message)

def raise_not_found(request: Request):
    """ Raise a 404 Not Found """
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)

def validate_and_check_url(target_url: str):
    """ Validate the URL format and check if it is reachable"""
    if not validators.url(target_url):
        raise_bad_requests(message="Your provided URL is not valid")
    try:
        response = httpx.get(target_url, timeout=5)
        if response.status_code >= 400:
            raise_bad_requests(message="The provided URL is unreachable")
    except httpx.RequestError as e:
        raise_bad_requests(message=f"The provided URL is unreachable: {str(e)}")
