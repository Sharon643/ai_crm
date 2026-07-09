from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    Time,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_id = Column(Integer, ForeignKey("hcps.id"))

    interaction_type = Column(String)

    interaction_date = Column(Date, nullable=True)

    interaction_time = Column(Time, nullable=True)

    attendees = Column(Text)

    topics = Column(Text)

    materials = Column(Text)

    sentiment = Column(String)

    outcome = Column(Text)

    follow_up = Column(Text)

    summary = Column(Text)

    hcp = relationship("HCP")

    action_items = relationship(
    "ActionItem",
    back_populates="interaction",
    cascade="all, delete-orphan",)