# Deploy-LLM-App-as-API
# FastAPI Language Model Server

This project is a simple API server built using FastAPI to interact with the Google Gemini model via the Langchain framework. The server supports generating essays based on a given topic through a language model powered by the `ChatGoogleGenerativeAI` API.

## Features

- **FastAPI**: A modern, fast web framework for building APIs.
- **Langchain**: Provides a framework for language models and easy integration with `Google Gemini`.
- **Google Gemini API**: Utilizes the `gemini-1.5-pro` model for language generation.
- **Custom Routes**: The API provides routes to generate essays based on topics provided by the user.

## Requirements

To run this project, ensure you have the following:

- Python 3.7+
- A valid Google API key for accessing Google Gemini (Language Models)
- FastAPI
- Uvicorn
- Langchain
- Langchain Google Generative AI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/lang-server.git
   cd lang-server
   ```
## Usage
### Running the API Server
### Start the FastAPI server:
```bash
python app.py
```
The server will start on http://localhost:8000.
## API Endpoints
1. /gemini
This route provides access to the raw Gemini model.

2. /essay
This route allows you to generate an essay based on a given topic. You can POST a JSON payload specifying the topic.

## Example: Using the Client
You can use the client.py to make a request to the /essay endpoint.
## Reference
1. https://python.langchain.com/docs/integrations/chat/google_generative_ai/
2. https://ai.google.dev/gemini-api/docs/api-key
3. https://smith.langchain.com/
4. https://python.langchain.com/docs/langserve/#using-add_routes
