from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# автоматически прогрузить переменные
load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")
resp = model.invoke("What is the capital of France?")
print(resp.content)