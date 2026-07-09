def route_message(message: str) -> str:
    message = message.lower().strip()

    edit_keywords = [
        "edit",
        "update",
        "change",
        "modify",
    ]

    meeting_keywords = [
        "prepare me",
        "meeting preparation",
        "meeting prep",
        "meeting brief",
        "brief me",
        "prepare for my meeting",
    ]

    planner_keywords = [
        "visit planner",
        "visit plan",
        "plan my visits",
        "plan today's visits",
        "today's visits",
        "today visits",
        "who should i visit",
        "who should i meet",
        "recommend visits",
    ]

    action_keywords = [
        "action items",
        "actions",
        "my actions",
        "pending actions",
        "pending action items",
        "tasks",
        "my tasks",
        "todo",
        "show my action items",
        "show my tasks",
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