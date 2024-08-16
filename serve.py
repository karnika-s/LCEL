# file created to write the implementation part 
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os 
from langserve import add_routes

from dotenv import load_dotenv
load_dotenv() 

groq_api_key=os.getenv("GROQ_API_KEY")

model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# this is the basic prompt from main
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])


parser =StrOutputParser()

# chaining 
chain= prompt_template |model |parser 

# app ka code 

app =FastAPI(title="langchain server", 
             version="1.0", 
             description = "api server using langchain interfaces")

# chain rout is being added here 
add_routes(
    app,
    chain,
    path="/chain"
)

# starting the app from here
if __name__ == "__main__":
    import uvicorn
    uvicorn.run( app, host="localhost", port=8000)


# python serve.py   ... command is used to run the file
# but if nothing is visible on localport then use /docs after the url of local 8000
# the chain is invoked this way 
