from typing import Literal

from pydantic import BaseModel


Priority = Literal[
    "High",
    "Medium",
    "Low",
]


class VisitRecommendation(BaseModel):
    hcp_id: int
    hcp_name: str
    hospital: str

    score: int

    priority: Priority

    reason: str


class VisitPlan(BaseModel):
    visits: list[VisitRecommendation]