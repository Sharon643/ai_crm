from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.hcp import HCP
from app.schemas.hcp import HCPCreate, HCPResponse

router = APIRouter(prefix="/hcp", tags=["HCP"])


@router.post("/", response_model=HCPResponse)
def create_hcp(data: HCPCreate, db: Session = Depends(get_db)):
    hcp = HCP(**data.model_dump())

    db.add(hcp)
    db.commit()
    db.refresh(hcp)

    return hcp


@router.get("/", response_model=list[HCPResponse])
def get_all_hcps(db: Session = Depends(get_db)):
    return db.query(HCP).all()