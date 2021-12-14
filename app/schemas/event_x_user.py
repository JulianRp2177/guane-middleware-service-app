from typing import Optional
from pydantic import BaseModel

class CreateEventXUser(BaseModel):
    event_id: int
    user_id : int

class UpdateEventXUser(BaseModel):
    event_id: Optional[int]
    user_id : Optional[int]

class PayloadEventXUser(BaseModel):
    event_id: Optional[int]
    user_id : Optional[int]

class EventXUserInDB(UpdateEventXUser):
    id: int

    class Config:
        orm_mode = True
