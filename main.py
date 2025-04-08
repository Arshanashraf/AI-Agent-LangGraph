from langgraph.graph import StateGraph
import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Annotated, List
from typing_extensions import TypedDict
import operator

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

class ChatState(TypedDict):
    query: Annotated[str , operator.add] 
    response: Annotated[str, operator.add] 
def query_gemini(prompt: str) -> str:
    response = model.generate_content([prompt])
    return response.text if response and hasattr(response, "text") else "Sorry, I couldn't generate a response."

def supervisor(state: ChatState):
    query = state["query"].lower()
    
    if "summarize" in query:
        return {"next": ["workerSummarizer"]}
    elif "analyze" in query:
        return {"next": ["workerAnalyzer"]}
    else:
        return {"next": ["workerGeneral"]}

def workerSummarizer(state: ChatState):
    response_text = query_gemini(state["query"])
    state["response"] = response_text  # Set the response directly
    return state

def workerAnalyzer(state: ChatState):
    response_text = query_gemini(state["query"])
    state["response"] = response_text  # Set the response directly
    return state

def workerGeneral(state: ChatState):
    response_text = query_gemini(state["query"])
    state["response"] = response_text  # Set the response directly
    return state

# Create the workflow using the StateGraph
workflow = StateGraph(ChatState)

# Add the nodes to the workflow
workflow.add_node("supervisor", supervisor)
workflow.add_node("workerSummarizer", workerSummarizer)
workflow.add_node("workerAnalyzer", workerAnalyzer)
workflow.add_node("workerGeneral", workerGeneral)

# Define the edges of the workflow
workflow.add_edge("supervisor", "workerSummarizer")
workflow.add_edge("supervisor", "workerAnalyzer")
workflow.add_edge("supervisor", "workerGeneral")

# Set the entry and termination points
workflow.set_entry_point("supervisor")
workflow.set_finish_point(["workerSummarizer", "workerAnalyzer", "workerGeneral"])

# Compile the workflow
compiled_workflow = workflow.compile()

# Initialize chat history to store the conversation
chat_history = []

# Execution loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    try:
        # Ensure 'query' is passed as a single value (string)
        state = {"query": user_input.strip(), "response": ""}  # Initialize with an empty response
        
        # Execute the workflow and get the result
        result = compiled_workflow.invoke(state)
        
        # Print the result from the AI
        print("AI:", result["response"])

        # Accumulate responses in the main loop
        chat_history.append(f"You: {user_input}")
        chat_history.append(f"AI: {result['response']}")
    
    except Exception as e:
        print("Error:", e)
