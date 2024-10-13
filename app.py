from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os

# Set the Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyB6e-fh4XssONmthsNLx0JnCTZcy2ZkaEo"

# Initialize the language model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
)

# Create the FastAPI app
app = FastAPI(
    title="lang server",
    version="1.0",
    description="A simple API server"
)

# Add routes for the language model
add_routes(
    app,
    llm,
    path="/gemini"
)

# Define the prompt template
prompt = ChatPromptTemplate.from_template("provide me essay about {topic}")

# Add routes for the prompt and model
add_routes(
    app,
    prompt | llm,
    path="/essay"
)

# Run the app
if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
