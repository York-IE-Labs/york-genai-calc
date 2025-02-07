from pydantic import BaseModel

class LLM(BaseModel):

    provider_id: str
    provider_name_pretty: str

    model_id: str
    model_name_pretty: str

    cost_per_1k_input_tokens: float
    cost_per_1k_output_tokens: float