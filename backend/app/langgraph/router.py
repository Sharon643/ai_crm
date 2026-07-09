def route_message(message: str) -> str:
    message = message.lower().strip()

    edit_keywords = [
        "edit",
        "update",
        "change",
        "modify",
    ]

    meeting_keywords = [
        "prepare",
        "meeting brief",
        "meeting preparation",
    ]

    planner_keywords = [
        "visit plan",
        "visit planner",
        "plan my visits",
        "today's visits",
    ]

    action_keywords = [
        "action items",
        "action item",
        "tasks",
        "to-do",
        "todo",
    ]

    if any(keyword in message for keyword in edit_keywords):
        return "edit"

    if any(keyword in message for keyword in meeting_keywords):
        return "meeting"

    if any(keyword in message for keyword in planner_keywords):
        return "planner"

    if any(keyword in message for keyword in action_keywords):
        return "actions"

    return "log"