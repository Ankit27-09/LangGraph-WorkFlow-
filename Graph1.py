# Graph - 1 
# Hello World Graph 🌍
# Objectives  :
# Understand and define the AgentState structure
# Create simple node functions to process and update state
# Set up a basic LangGraph structure
# Compile and invoke a LangGraph graph
# Understand how data flows through a single-node in LangGraph

from typing import Dict, TypedDict
from langgraph.graph import StateGraph #framework that helps you design and manage the flow of tasks in your application using a graph structure

# We now create an AgentState - shared data structure that keeps track of information as your application runs

class AgentState(TypedDict):
  message: str

def greeting_node(state : AgentState) -> AgentState:
  """ Simple node that adds a greeting message to the state """

  state['message'] = "Hey " + state["message"] + ", how is your day going?"
  return state

graph = StateGraph(AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"message": "Bob"})
result["message"]
