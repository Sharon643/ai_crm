from langchain_core.messages import HumanMessage, SystemMessage

from app.ai.llm import llm

from app.ai.prompts import (
    EDIT_INTERACTION_PROMPT,
)

from app.schemas.edit_interaction import (
    EditInteraction,
)

structured_llm = llm.with_structured_output(
    EditInteraction
)


def extract_edit(text: str):
    return structured_llm.invoke(
        [
            SystemMessage(
                content=EDIT_INTERACTION_PROMPT
            ),
            HumanMessage(content=text),
        ]
    )