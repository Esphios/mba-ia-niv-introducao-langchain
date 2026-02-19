from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

system = ("system", "you are an assistant that answers questions in a {style} style. Be concise and creative.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="funny", question="Tell me a joke about my name (Eduardo)")

for msg in messages:
    print(f"{msg.type}: {msg.content}")

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)
result = model.invoke(messages)
print(result.content)
