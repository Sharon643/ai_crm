from sqlalchemy.orm import Session

from app.models.interaction import Interaction


def create_interaction(db: Session, data: dict):

    interaction = Interaction(
        **data
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_interaction_history(
    db: Session,
    hcp_id: int,
):
    return (
        db.query(Interaction)
        .filter(
            Interaction.hcp_id == hcp_id
        )
        .order_by(
            Interaction.interaction_date.desc()
        )
        .all()
    )


def update_interaction(
    db: Session,
    interaction_id: int,
    updates: dict,
):
    interaction = (
        db.query(Interaction)
        .filter(
            Interaction.id == interaction_id
        )
        .first()
    )

    if not interaction:
        return None

    for key, value in updates.items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction