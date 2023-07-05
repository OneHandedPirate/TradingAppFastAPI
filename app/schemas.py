import uuid
from datetime import datetime

from pydantic import BaseModel


class OperationResponse(BaseModel):
    id: uuid.UUID
    type: str
    quantity: str
    figi: str
    instrument_type: str
    date: datetime

    class Config:
        orm_mode = True


class OperationCreate(BaseModel):
    quantity: str
    figi: str
    instrument_type: str
    type: str
