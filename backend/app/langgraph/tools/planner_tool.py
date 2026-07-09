from langchain_core.tools import tool

from app.schemas.tools_response import ToolResponse

from app.database.database import SessionLocal

from app.services.visit_planner_service import (
    build_visit_plan,
)


@tool
def visit_planner(user_input: str):
    """
    Generate today's recommended visit plan.
    """

    db = SessionLocal()

    try:

        visits = build_visit_plan(db)

        return ToolResponse(
            type="planner",
            success=True,
            message="""
            I've analyzed your interaction history, pending action items, and follow-ups.

            Your personalized visit plan is ready.

            Opening Visit Planner...
            """,
            payload={
                "visits": visits
            },
        )

    finally:
        db.close()