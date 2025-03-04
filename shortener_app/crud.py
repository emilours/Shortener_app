from sqlalchemy.orm import Session
from . import schemas, models, keygen

def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    """ create a a new shortened URL in the database """
    key = keygen.create_unique_random_key(db)
    secret_key = f"{key}_{keygen.create_random_key(length=8)}"
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    print(f"Created URL: {db_url.target_url} with key {db_url.key}")
    return db_url

def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    """ Get an active URL from the database by key """
    return (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )

def get_db_url_by_secret_key(db: Session, secret_key: str) -> models.URL:
    """ Get an active URL from the database by secret key """
    return (
        db.query(models.URL)
        .filter(models.URL.secret_key == secret_key, models.URL.is_active)
        .first()
    )

def update_db_clicks(db: Session, db_url: schemas.URL) -> models.URL:
    """ Update the clicks for a given URL """
    db_url.clicks += 1
    db.commit()
    db.refresh(db_url)
    return db_url

def deactivate_db_url_by_secret_key(db: Session, secret_key: str) -> models.URL:
    """ Deactivate a URL by secret key """
    db_url = get_db_url_by_secret_key(db, secret_key)
    if db_url:
        db_url.is_active = False
        db.commit()
        db.refresh(db_url)
    return db_url