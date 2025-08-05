import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_openai_model(
    model_id: str = "gpt-4o",
    max_tokens: int = 500
) -> ChatOpenAI:
    return ChatOpenAI(
        model=model_id,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        max_tokens=max_tokens
    )

# Preconfigured
gpt_4o = get_openai_model()
