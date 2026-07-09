from sqlalchemy.orm import Session

from app.models.hcp import HCP
from app.models.action_item import ActionItem
from app.models.interaction import Interaction


def build_visit_plan(db: Session):

    visits = []

    hcps = db.query(HCP).all()

    for hcp in hcps:

        score = 0

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

        if latest is None:
            continue

        if latest.follow_up:
            score += 25

        if latest.sentiment == "Negative":
            score += 20

        elif latest.sentiment == "Neutral":
            score += 10

        actions = (
            db.query(ActionItem)
            .filter(
                ActionItem.hcp_id == hcp.id,
                ActionItem.status == "Pending",
            )
            .all()
        )

        reason = []

        high = 0
        medium = 0
        low = 0

        for action in actions:

            if action.priority == "High":
                score += 20
                high += 1

            elif action.priority == "Medium":
                score += 10
                medium += 1

            else:
                score += 5
                low += 1

        if latest.follow_up:
            reason.append("Follow-up scheduled")

        if high:
            reason.append(
                f"{high} high priority action item(s)"
            )

        if medium:
            reason.append(
                f"{medium} medium priority action item(s)"
            )

        if latest.sentiment == "Negative":
            reason.append(
                "Previous interaction was negative"
            )

        if score >= 80:
            priority = "High"

        elif score >= 50:
            priority = "Medium"

        else:
            priority = "Low"

        visits.append(
            {
                "hcp_id": hcp.id,
                "hcp_name": hcp.name,
                "hospital": hcp.hospital,
                "score": score,
                "priority": priority,
                "reason": ", ".join(reason)
                if reason
                else "Routine visit",
            }
        )

    visits.sort(
        key=lambda x: x["score"],
        reverse=True,
    )

    return visits