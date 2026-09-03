## Purpose : Creating an Agent
import os
from dotenv import load_dotenv
import langchain
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from app.Agent.toolproduct import(
    search_product_categories,
    get_all_product_categories,
    search_product_on_name_Service,
    search_product_on_description_Service,
    search_product_on_brand_Service,
    get_product_List_For_Given_Category_Service,
    is_stockavilableforproduct_Service,
)
 
from app.Agent.toolcustomer import get_customer_by_phone

from app.Agent.prompts import SYSTEM_PROMPT

load_dotenv()

## OLLAMA Model Refrence
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
 
if not OLLAMA_MODEL:
    raise ValueError("OLLAMA_MODEL is not configured")

model = ChatOllama(model=OLLAMA_MODEL,temperature=0)

## Tool configuration
tools = [
    get_all_product_categories,
    search_product_categories,
    search_product_on_name_Service,
    search_product_on_description_Service,
    search_product_on_brand_Service,
    get_product_List_For_Given_Category_Service,
    is_stockavilableforproduct_Service,
    get_customer_by_phone
]



## Create an Agent
agent = create_agent(model=model,tools=tools,system_prompt=SYSTEM_PROMPT)

## Chat Function
def chat(message: str) -> str:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "Customer",
                    "content": message
                }
            ]
        }
    )

    return result["messages"][-1].content

## Only for Test 
if __name__ == "__main__":

    print("Catboat started.")
    print("Type 'exit' to stop.")

    while True:

        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            break

        response = chat(user_message)

        print("Catboat:", response)