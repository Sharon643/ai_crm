from datetime import date, time

from pydantic import BaseModel


class InteractionCreate(BaseModel):
    hcpName: str
    hospital: str

    interactionType: str

    date: date
    time: time

    attendees: str

    topics: str
    materials: str

    sentiment: str
    outcome: str

    followUp: str

    summary: str


class InteractionResponse(InteractionCreate):
    id: int

    class Config:
        from_attributes = True