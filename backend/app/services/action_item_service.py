from sqlalchemy.orm import Session

from app.models.action_item import ActionItem
from app.schemas.action_extraction import ActionExtraction
from collections import defaultdict

from app.models.action_item import ActionItem
from app.models.hcp import HCP


def create_action_items(
    db: Session,
    extraction: ActionExtraction,
    interaction_id: int,
    hcp_id: int,
):
    """
    Replace all action items for an interaction with a fresh AI extraction.
    """

    # Remove existing tasks for this interaction
    (
        db.query(ActionItem)
        .filter(
            ActionItem.interaction_id == interaction_id
        )
        .delete()
    )

    created_items = []

    for task in extraction.tasks:
        item = ActionItem(
            interaction_id=interaction_id,
            hcp_id=hcp_id,
            title=task.title,
            priority=task.priority,
            status="Pending",
            due_date=task.due_date,
        )

        db.add(item)
        created_items.append(item)

    db.commit()

    for item in created_items:
        db.refresh(item)

    return created_items




def get_action_items_grouped(db: Session):
    """
    Return all action items grouped by HCP.
    """

    items = (
        db.query(ActionItem)
        .join(HCP)
        .order_by(HCP.name)
        .all()
    )

    grouped = defaultdict(
        lambda: {
            "hcp": None,
            "pending": 0,
            "completed": 0,
            "tasks": [],
        }
    )

    for item in items:

        group = grouped[item.hcp.id]

        if group["hcp"] is None:
            group["hcp"] = {
                "id": item.hcp.id,
                "name": item.hcp.name,
                "hospital": item.hcp.hospital,
            }

        task = {
            "id": item.id,
            "title": item.title,
            "priority": item.priority,
            "status": item.status,
            "due_date": item.due_date,
        }

        group["tasks"].append(task)

        if item.status == "Pending":
            group["pending"] += 1
        else:
            group["completed"] += 1

    return list(grouped.values())

def update_action_status(
    db: Session,
    action_id: int,
    status: str,
):
    action = (
        db.query(ActionItem)
        .filter(ActionItem.id == action_id)
        .first()
    )

    if not action:
        return None

    action.status = status

    db.commit()

    db.refresh(action)

    return action