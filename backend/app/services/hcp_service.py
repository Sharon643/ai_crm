from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.hcp import HCP


def get_hcp_by_name(db: Session, name: str):
    return (
        db.query(HCP)
        .filter(func.lower(HCP.name) == name.lower())
        .first()
    )


def create_hcp(
    db: Session,
    name: str,
    hospital: str,
    specialization: str = "",
):
    hcp = HCP(
        name=name,
        hospital=hospital,
        specialization=specialization,
    )

    db.add(hcp)
    db.commit()
    db.refresh(hcp)

    return hcp


def get_all_hcps(db: Session):
    return db.query(HCP).all()