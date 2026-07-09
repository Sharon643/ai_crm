from typing import TypedDict

from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.langgraph.router import route_message

from app.langgraph.tools import (
    log_interaction,
    edit_interaction,
    meeting_preparation,
    visit_planner,
    action_items,
)


class GraphState(TypedDict):
    message: str
    tool: str
    result: dict


def router_node(state: GraphState):

    tool = route_message(state["message"])

    # print("=" * 60)
    # print("MESSAGE :", state["message"])
    # print("ROUTE   :", tool)
    # print("=" * 60)

    return {
        **state,
        "tool": tool,
    }


def log_node(state: GraphState):

    result = log_interaction.invoke(
        {
            "user_input": state["message"],
        }
    )

    return {
        **state,
        "result": result,
    }


def edit_node(state: GraphState):

    result = edit_interaction.invoke(
        {
            "user_input": state["message"],
        }
    )

    return {
        **state,
        "result": result,
    }

def planner_node(state):

    result = visit_planner.invoke(
        {
            "user_input": state["message"]
        }
    )

    return {
        **state,
        "result": result,
    }

def meeting_node(state):

    result = meeting_preparation.invoke(
        {
            "user_input": state["message"]
        }
    )

    return {
        **state,
        "result": result,
    }

def actions_node(state):
    result = action_items.invoke(
        {
            "user_input": state["message"],
        }
    )

    return {
        **state,
        "result": result,
    }

builder = StateGraph(GraphState)

builder.add_node("router", router_node)
builder.add_node("log", log_node)
builder.add_node("edit", edit_node)
builder.add_node("planner",planner_node,)
builder.add_node("meeting",meeting_node,)
builder.add_node("actions", actions_node)

builder.add_edge(START, "router")

builder.add_conditional_edges(
    "router",
    lambda state: state["tool"],
    {
        "log": "log",
        "edit": "edit",
        "planner": "planner",
        "meeting": "meeting",
        "actions": "actions",
    },
)

builder.add_edge("log", END)
builder.add_edge("edit", END)
builder.add_edge("planner", END)
builder.add_edge("meeting",END,)
builder.add_edge("actions", END)


graph = builder.compile()