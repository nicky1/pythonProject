import os
os.environ['OPENAI_API_KEY']='sess-ytGZpQmYjyGN5YlTattZU3oYlHsztmNbp4zoLrc7'
from langchain.llms import OpenAI
# 使用langchain包调用OpenAI的text模型
llm = OpenAI(
    model="text-davinci-003",
    temperature=0.5,
    max_tokens=60,)
response = llm.predict("请给我的花店起个名")
print(response)