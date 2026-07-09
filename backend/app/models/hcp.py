from sqlalchemy import Column, Integer, String
from app.database.database import Base


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    specialization = Column(String)

    hospital = Column(String)