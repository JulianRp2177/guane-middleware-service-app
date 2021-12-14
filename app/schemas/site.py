from typing import Optional
from pydantic import BaseModel

class CreateSite(BaseModel):
    name : str
    direction : Optional[str]
    description : Optional[str]
    schedule : Optional[str]

class UpdateSite(BaseModel):
    name : Optional[str]
    direction : Optional[str]
    description : Optional[str]
    schedule : Optional[str]

class PayloadSite(BaseModel):
    name : Optional[str]
    direction : Optional[str]
    description : Optional[str]
    schedule : Optional[str]

class SiteInDB(UpdateSite):
    id: int

    class Config:
        orm_mode = True
