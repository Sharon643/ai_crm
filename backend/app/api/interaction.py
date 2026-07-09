from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.hcp import HCP
from app.models.interaction import Interaction

from app.schemas.interaction import InteractionCreate

router = APIRouter(
    prefix="/interaction",
    tags=["Interaction"],
)


@router.post("/")
def create_interaction_api(
    request: InteractionCreate,
    db: Session = Depends(get_db),
):
    # Find existing HCP
    hcp = (
        db.query(HCP)
        .filter(HCP.name == request.hcpName)
        .first()
    )

    # Create HCP if not found
    if not hcp:
        hcp = HCP(
            name=request.hcpName,
            hospital=request.hospital,
        )

        db.add(hcp)
        db.commit()
        db.refresh(hcp)

    # Save interaction
    interaction = Interaction(
        hcp_id=hcp.id,
        interaction_type=request.interactionType,
        interaction_date=request.date,
        interaction_time=request.time,
        attendees=request.attendees,
        topics=request.topics,
        materials=request.materials,
        sentiment=request.sentiment,
        outcome=request.outcome,
        follow_up=request.followUp,
        summary=request.summary,
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "success": True,
        "message": "Interaction saved successfully.",
        "interaction_id": interaction.id,
    }