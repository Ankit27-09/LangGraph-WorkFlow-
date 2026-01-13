"""**GRAPH -2**"""
# Multiple Inputs Graph 
# Objectives:
# Define a more complex AgentState
# Create a processing node that performs operations on list data
# Set up a LangGraph that processes and outputs computed results
# Invoke the graph with structured inputs and retrieve outputs


from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):  # State Schema
    values: List[int]
    name: str
    result: str

def process_val(state: AgentState) -> AgentState:
  """This function handles multiple different inputs"""
  print(state)
  state["result"] = f"Hi there {state["name"]}! Your sum = {sum(state["values"])}"
  print(state)
  return state

graph = StateGraph(AgentState)

graph.add_node("processor", process_val)
graph.set_entry_point("processor") # Set the starting node
graph.set_finish_point("processor") # Set the ending node

app = graph.compile() # Compiling the graph

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

answers = app.invoke({"values": [1,2,3,4], "name": "Steve"})