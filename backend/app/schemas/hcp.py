from pydantic import BaseModel


class HCPCreate(BaseModel):
    name: str
    specialization: str
    hospital: str


class HCPResponse(HCPCreate):
    id: int

    class Config:
        from_attributes = True