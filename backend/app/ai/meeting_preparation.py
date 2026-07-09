import json

from app.ai.llm import llm

from app.ai.prompts import (
    MEETING_PREPARATION_PROMPT,
)


def generate_meeting_brief(context):

    latest = context["latest_interaction"]

    payload = {
        "doctor": context["doctor"],
        "hospital": context["hospital"],
        "topics": latest.topics,
        "materials": latest.materials,
        "outcome": latest.outcome,
        "follow_up": latest.follow_up,
        "pending_actions": [
            a.title for a in context["actions"]
        ],
    }

    prompt = f"""
{MEETING_PREPARATION_PROMPT}

{json.dumps(payload, indent=2)}
"""

    return llm.invoke(prompt).content