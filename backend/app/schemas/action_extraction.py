from typing import Literal

from pydantic import BaseModel


Priority = Literal[
    "High",
    "Medium",
    "Low",
]


class ExtractedAction(BaseModel):
    title: str
    priority: Priority
    due_date: str | None = None


class ActionExtraction(BaseModel):
    tasks: list[ExtractedAction]