from enum import Enum

from pydantic import BaseModel


class Route(str, Enum):
    log = "log"
    edit = "edit"
    meeting = "meeting"
    planner = "planner"
    actions = "actions"


class RouteDecision(BaseModel):
    tool: Route