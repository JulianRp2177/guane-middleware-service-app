from typing import Optional
from pydantic import BaseModel

class CreateEvent(BaseModel):
    name: str
    meeting_time: str
    description: Optional[str]
    reservation: Optional[bool]
    quantity: Optional[int]
    trainer_id : int
    site_id : int

class UpdateEvent(BaseModel):
    name: Optional[str]
    meeting_time: Optional[str]
    description: Optional[str]
    reservation: Optional[bool]
    quantity: Optional[int]
    trainer_id : Optional[int]
    site_id : Optional[int]

class PayloadEvent(BaseModel):
    name: Optional[str]
    meeting_time: Optional[str]
    description: Optional[str]
    reservation: Optional[bool]
    quantity: Optional[int]
    trainer_id : Optional[int]
    site_id : Optional[int]

class EventInDB(UpdateEvent):
    id: int

    class Config:
        orm_mode = True
