from pydantic import BaseModel


class InteractionExtraction(BaseModel):
    hcpName: str = ""
    hospital: str = ""
    interactionType: str = ""

    date: str = ""
    time: str = ""

    attendees: str = ""

    topics: str = ""
    materials: str = ""

    sentiment: str = ""
    outcome: str = ""

    followUp: str = ""

    summary: str = ""