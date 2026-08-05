from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# автоматически прогрузить переменные
load_dotenv()

model = ChatOpenAI(model="gpt-5.4-pro", temperature=1, timeout=(10, 120), max_retries=0)
resp = model.invoke([
    SystemMessage(content="You are an experienced linguist specializing in Slavic languages"),
    HumanMessage(content="Say 'Good day, cat!' in three languages")
])
print(resp.response_metadata)
print(resp.content)