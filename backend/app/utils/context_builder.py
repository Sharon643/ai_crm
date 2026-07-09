from app.models.hcp import HCP
from app.models.interaction import Interaction


def build_interaction_context(
    hcp: HCP,
    interaction: Interaction,
) -> str:
    """
    Build a consistent textual representation of an interaction
    for downstream AI tools.
    """

    return f"""
Healthcare Professional:
{hcp.name}

Hospital:
{hcp.hospital}

Interaction Type:
{interaction.interaction_type}

Interaction Date:
{interaction.interaction_date}

Interaction Time:
{interaction.interaction_time}

Attendees:
{interaction.attendees}

Topics Discussed:
{interaction.topics}

Materials Shared:
{interaction.materials}

Sentiment:
{interaction.sentiment}

Outcome:
{interaction.outcome}

Follow-up:
{interaction.follow_up}
"""