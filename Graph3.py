#  Graph 3 

# Sequential Graph ∞
# Objectives:
# Create multiple Nodes that sequentially process and update different parts of the state.
# Connect Nodes together in a graph
# Invoke the Graph and see how the state is transformed step-by-step.
# Main Goal: Create and handle multiple Nodes

from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
  name: str
  age: int
  final: str

def first_node(state:AgentState) -> AgentState:
    """This is the first node of our sequence"""

    state["final"] = f"Hi {state["name"]}!"
    return state

def second_node(state:AgentState) -> AgentState:
    """This is the second node of our sequence"""

    state["final"] = state["final"] + f" You are {state["age"]} years old!"

    return state

graph = StateGraph(AgentState)

graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")
app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"name": "Charlie", "age": 20})
print(result)