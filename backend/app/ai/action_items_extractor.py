from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from app.ai.llm import llm

from app.ai.prompts import (
    ACTION_ITEMS_PROMPT,
)

from app.schemas.action_extraction import (
    ActionExtraction,
)

structured_llm = llm.with_structured_output(
    ActionExtraction
)


def extract_action_items(text: str):

    return structured_llm.invoke(
        [
            SystemMessage(
                content=ACTION_ITEMS_PROMPT
            ),
            HumanMessage(
                content=text
            ),
        ]
    )