from csv import DictReader

from york_genai_calc.config import paths
from york_genai_calc.mappings.llms import get_model_pretty_name_from_id
from york_genai_calc.mappings.providers import get_provider_pretty_name_from_id
from york_genai_calc.models.llm import LLM

def create_llm_pricing_from_def(llm_def: dict) -> LLM:

    model_id = llm_def['model_id']
    provider_id = model_id.split('.', 1)[0]

    model_name_pretty = get_model_pretty_name_from_id(model_id)
    provider_name_pretty = get_provider_pretty_name_from_id(provider_id)

    return LLM(
        provider_id=provider_id,
        provider_name_pretty=provider_name_pretty,
        model_id=model_id,
        model_name_pretty=model_name_pretty,
        cost_per_1k_input_tokens=llm_def['cost_per_1k_input_tokens'],
        cost_per_1k_output_tokens=llm_def['cost_per_1k_output_tokens']
    )

with (paths.ASSETS_FOLDER / "pricing.csv").open() as f_in:
    PRICING_MAPPING: dict[str, LLM] = {
        llm.model_id: llm
        for llm in
        map(create_llm_pricing_from_def, DictReader(f_in))
    }

def get_llm_pricing_from_model_id(model_id: str) -> LLM:
    return PRICING_MAPPING[model_id]


if __name__ == "__main__":
    print(PRICING_MAPPING)