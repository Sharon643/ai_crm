from sqlalchemy.orm import Session

from app.models.hcp import HCP
from app.models.interaction import Interaction
from app.models.action_item import ActionItem


def get_meeting_context(db: Session, doctor_name: str):

    hcp = (
        db.query(HCP)
        .filter(HCP.name.ilike(f"%{doctor_name}%"))
        .first()
    )

    if not hcp:
        return None

    latest = (
        db.query(Interaction)
        .filter(
            Interaction.hcp_id == hcp.id
        )
        .order_by(
            Interaction.id.desc()
        )
        .first()
    )

    actions = (
        db.query(ActionItem)
        .filter(
            ActionItem.hcp_id == hcp.id,
            ActionItem.status == "Pending"
        )
        .all()
    )

    return {
        "doctor": hcp.name,
        "hospital": hcp.hospital,
        "latest_interaction": latest,
        "actions": actions,
    }