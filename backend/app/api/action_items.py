from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.action_item import (
    ActionStatusUpdate,
)

from app.services.action_item_service import (
    get_action_items_grouped,
    update_action_status,
)

router = APIRouter(
    prefix="/action-items",
    tags=["Action Items"],
)


@router.get("/")
def get_action_items(
    db: Session = Depends(get_db),
):
    return get_action_items_grouped(db)


@router.patch("/{action_id}")
def update_action_item(
    action_id: int,
    request: ActionStatusUpdate,
    db: Session = Depends(get_db),
):

    action = update_action_status(
        db,
        action_id,
        request.status,
    )

    if action is None:
        raise HTTPException(
            status_code=404,
            detail="Action item not found.",
        )

    return {
        "success": True,
        "message": "Action item updated.",
    }