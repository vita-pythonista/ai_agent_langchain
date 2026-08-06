from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# автоматически прогрузить переменные
load_dotenv()

task_template = "Say '{text}' in three languages"
task = task_template.format(text=input("Input something in Russian: "))

model = ChatOpenAI(model="gpt-4.1-mini", temperature=1, timeout=(10, 120), max_retries=0)
resp = model.invoke([
    SystemMessage(content="You are an experienced linguist specializing in Slavic languages"),
    HumanMessage(content=task)
])
print(resp.response_metadata)
print(resp.content)