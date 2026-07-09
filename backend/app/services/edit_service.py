from sqlalchemy.orm import Session

from app.models.hcp import HCP
from app.models.interaction import Interaction


FIELD_MAPPING = {
    "sentiment": "sentiment",
    "topics": "topics",
    "materials": "materials",
    "outcome": "outcome",
    "followUp": "follow_up",
}


def edit_interaction(
    db: Session,
    hcp_name: str,
    field: str,
    value: str,
):
    hcp = (
        db.query(HCP)
        .filter(HCP.name == hcp_name)
        .first()
    )

    if not hcp:
        return {
            "success": False,
            "message": "HCP not found.",
        }

    interaction = (
        db.query(Interaction)
        .filter(
            Interaction.hcp_id == hcp.id
        )
        .order_by(
            Interaction.interaction_date.desc()
        )
        .first()
    )

    if not interaction:
        return {
            "success": False,
            "message": "No interaction found.",
        }

    db_field = FIELD_MAPPING.get(field)

    if not db_field:
        return {
            "success": False,
            "message": "Invalid field.",
        }

    setattr(interaction, db_field, value)

    db.commit()

    return {
        "success": True,
        "message": f"{field} updated successfully."
    }