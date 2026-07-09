from typing import Literal

from pydantic import BaseModel


Priority = Literal[
    "High",
    "Medium",
    "Low",
]

Status = Literal[
    "Pending",
    "Completed",
]


class ActionItemCreate(BaseModel):
    title: str
    priority: Priority
    due_date: str | None = None


class ActionItemResponse(BaseModel):
    id: int
    interaction_id: int
    hcp_id: int

    title: str

    priority: Priority

    status: Status

    due_date: str | None = None

    class Config:
        from_attributes = True