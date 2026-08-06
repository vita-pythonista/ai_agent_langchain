from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# автоматически прогрузить переменные
load_dotenv()

prompt_template = ChatPromptTemplate([
    ("system", "You are an experienced linguist specializing in {lang_kind} languages"),
    ("human", "Say '{text}' in three languages"),
])

prompt = prompt_template.format(lang_kind=input("Please enter your language kind: "),
                                text=input("Please enter your text: "))

model = ChatOpenAI(model="gpt-4.1-mini", temperature=1, timeout=(10, 120), max_retries=0)
resp = model.invoke(prompt)

print(resp.response_metadata)
print(resp.content)