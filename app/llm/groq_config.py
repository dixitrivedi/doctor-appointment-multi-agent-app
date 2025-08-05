import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_groq_model(
    model_id: str = "llama-3.1-70b-versatile",
    max_tokens: int = 500
) -> ChatGroq:
    return ChatGroq(
        model=model_id,
        groq_api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=max_tokens
    )

# Preconfigured model
llama_70b = get_groq_model()
