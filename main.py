from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# автоматически прогрузить переменные
load_dotenv()

prompt_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("prompts/system.txt", input_variables=["lang_kind"]),
    HumanMessagePromptTemplate.from_template("Say '{text}' in three languages")
])

prompt = prompt_template.format(lang_kind=input("Please enter your language kind: "),
                                text=input("Please enter your text: "))

model = ChatOpenAI(model="gpt-4.1-mini", temperature=1, timeout=(10, 120), max_retries=0)
resp = model.invoke(prompt)

print(resp.response_metadata)
print(resp.content)