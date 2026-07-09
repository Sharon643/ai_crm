from langchain_core.messages import HumanMessage, SystemMessage

from app.ai.llm import llm
from app.ai.prompts import EXTRACTION_PROMPT , EDIT_INTERACTION_PROMPT
from app.schemas.extraction import InteractionExtraction

structured_llm = llm.with_structured_output(
    InteractionExtraction
)


def extract_interaction(text: str) -> InteractionExtraction:
    return structured_llm.invoke(
        [
            SystemMessage(content=EXTRACTION_PROMPT),
            HumanMessage(content=text),
        ]
    )
