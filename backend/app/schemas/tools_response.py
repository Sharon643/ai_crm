from typing import Any

from pydantic import BaseModel


class ToolResponse(BaseModel):
    type: str
    success: bool
    message: str
    payload: Any | None = None