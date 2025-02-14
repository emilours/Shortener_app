from pydantic import BaseModel

class URLBase(BaseModel):
    """ Base URL model """
    target_url: str

class URL(URLBase):
    """ URL model """
    is_active: bool
    clicks: int

    class Config:
        """ Pydantic configuration """
        orm_mode = True

class URLInfo(URL):
    """ URL Info model """
    url: str
    admin_url: str