from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# автоматически прогрузить переменные
load_dotenv()

language = "arabic"
tone = "friendly"

values = {
    "language": input(f"Please enter your language: (default:{language}) ".strip()) or language,
    "tone": input(f"Please enter your tone: (default:{tone}) ".strip()) or tone,
    "text": input("Please enter your text: ")
}

prompt_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("prompts/system.txt", input_variables=["language"]),
    SystemMessagePromptTemplate.from_template("Your tone of conversations is {tone}"),
    HumanMessagePromptTemplate.from_template("Say '{text}' in three languages")
])

prompt = prompt_template.format(**values)

model = ChatOpenAI(model="gpt-4.1-mini", temperature=1, timeout=(10, 120), max_retries=0)
resp = model.invoke(prompt)

print(resp.response_metadata)
print(resp.content)