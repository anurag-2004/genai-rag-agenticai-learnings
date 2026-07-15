import os

os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

import os

llm = ChatOpenAI(model="gpt-4.1")
history=[]
while True:
    query=input("user: ")
    if query.lower() == "exit":
        print("Exiting the chat...")
        break
    history.append({"role": "user", "content": query})
    response = llm.invoke(history)

    print("AI:",response.content)
    history.append({"role": "assistant", "content": response.content})

print("\n\n\n",history,"\n\n\n")
