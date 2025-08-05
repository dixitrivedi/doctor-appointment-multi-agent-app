from app.llm.openai_config import gpt_4o
from app.llm.groq_config import llama_70b

class LLMFactory:
    __models = {
        "gpt-4o": gpt_4o,
        "llama-70b": llama_70b,
    }

    @classmethod
    def get_model(cls, model_id: str):
        model = cls.__models.get(model_id)
        if not model:
            raise ValueError(f"Model '{model_id}' not supported. Available: {list(cls.__models.keys())}")
        return model

    @classmethod
    def supported_models(cls):
        return list(cls.__models.keys())
