import os
os.environ["OPENAI_API_KEY"] = 'sess-ytGZpQmYjyGN5YlTattZU3oYlHsztmNbp4zoLrc7'
from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI(model="gpt-3.5-turbo",
                    temperature=0.8,
                    max_tokens=60)
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
messages = [
    SystemMessage(content="你是一个很棒的智能助手"),
    HumanMessage(content="请给我的花店起个名")
]
response = chat(messages)
print(response)