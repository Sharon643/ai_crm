from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class ActionItem(Base):
    __tablename__ = "action_items"

    id = Column(Integer, primary_key=True, index=True)

    interaction_id = Column(
        Integer,
        ForeignKey("interactions.id"),
        nullable=False,
    )

    hcp_id = Column(
        Integer,
        ForeignKey("hcps.id"),
        nullable=False,
    )

    title = Column(
        String,
        nullable=False,
    )

    priority = Column(
        String,
        nullable=False,
    )

    status = Column(
        String,
        default="Pending",
    )

    due_date = Column(
        String,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )
    updated_at = Column(
    DateTime,
    default=datetime.utcnow,
    onupdate=datetime.utcnow,
    )

    interaction = relationship(
        "Interaction",
        back_populates="action_items",
    )

    hcp = relationship(
        "HCP",
        back_populates="action_items",
    )