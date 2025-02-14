from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
import validators
import httpx
from sqlalchemy.orm import Session
from . import schemas, models, crud
from .keygen import validate_and_check_url, raise_not_found
from .database import SessionLocal, engine
from starlette.datastructures import URL
from .config import get_settings

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    """ Get the database session """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    """ Default route for the application """
    return "Welcome to the URL Shortener!"

@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    """ Create a new shortened URL """
    if not url.target_url:
        raise HTTPException(status_code=400, detail="URL is required")
    validate_and_check_url(url.target_url)
    db_url = crud.create_db_url(db=db, url=url)
    return get_admin_info(db_url)


@app.get("/{url_key}")
def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    """ Redirect to the original URL """
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        crud.update_db_clicks(db=db, db_url=db_url)
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)

@app.get(
    "/admin/{secret_key}",
    name="administration info",
    response_model=schemas.URLInfo,
)
def get_url_info(
    secret_key: str, request: Request, db: Session = Depends(get_db)
):
    """ Get the admin details for the URL """
    if db_url := crud.get_db_url_by_secret_key(db, secret_key=secret_key):
        return get_admin_info(db_url)
    else:
        raise_not_found(request)

def get_admin_info(db_url: models.URL) -> schemas.URLInfo:
    """ Get the admin information for the URL """
    base_url = URL(get_settings().base_url)
    admin_endpoint = app.url_path_for(
        "administration info", secret_key=db_url.secret_key
    )
    db_url.url = str(base_url.replace(path=db_url.key))
    db_url.admin_url = str(base_url.replace(path=admin_endpoint))
    return db_url

@app.delete("/admin/{secret_key}")
def delete_url(
    secret_key: str, request: Request, db: Session = Depends(get_db)
):
    """ deactivate the shortened URL """
    if db_url := crud.deactivate_db_url_by_secret_key(db, secret_key=secret_key):
        message = f"Successfully deleted shortened URL for '{db_url.target_url}'"
        return {"detail": message}
    else:
        raise_not_found(request)