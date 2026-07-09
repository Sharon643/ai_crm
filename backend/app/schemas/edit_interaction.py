from enum import Enum

from pydantic import BaseModel


class EditableField(str, Enum):
    hcpName = "hcpName"
    interactionType = "interactionType"
    date = "date"
    time = "time"
    attendees = "attendees"
    topics = "topics"
    materials = "materials"
    sentiment = "sentiment"
    outcome = "outcome"
    followUp = "followUp"


class EditInteraction(BaseModel):
    field: EditableField
    value: str