from typing import Optional
from pydantic import BaseModel

class CreateTrainer(BaseModel):
    username: str
    password: str
    document: str
    speciality: Optional[str]
    email: Optional[str]
    phone: Optional[str]

class UpdateTrainer(BaseModel):
    username: Optional[str]
    password: Optional[str]
    document: Optional[str]
    speciality: Optional[str]
    email: Optional[str]
    phone: Optional[str]

class PayloadTrainer(BaseModel):
    username: Optional[str]
    password: Optional[str]
    document: Optional[str]
    speciality: Optional[str]
    email: Optional[str]
    phone: Optional[str]

class TrainerInDB(UpdateTrainer):
    id: int

    class Config:
        orm_mode = True
