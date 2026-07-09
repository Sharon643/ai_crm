FIELD_LABELS = {
    "hcpName": "Healthcare Professional",
    "interactionType": "interaction type",
    "date": "date",
    "time": "time",
    "attendees": "attendees",
    "topics": "discussion topics",
    "materials": "materials shared",
    "sentiment": "sentiment",
    "outcome": "interaction outcome",
    "followUp": "follow-up",
}


def build_edit_message(field: str, value: str) -> str:
    label = FIELD_LABELS.get(field, field)

    return (
        f"I've updated the {label} to '{value}'. "
        "The interaction form has been updated. "
        "Please review the changes before saving."
    )