from york_genai_calc.mappings import MODEL_NAME_MAPPING, PRICING_MAPPING, PROVIDER_NAME_MAPPING


def get_all_model_ids() -> list[str]:
    return sorted(MODEL_NAME_MAPPING.keys())

def get_model_name_mapping() -> dict[str, str]:
    return MODEL_NAME_MAPPING

def get_provider_mapping() -> dict[str, str]:
    return PROVIDER_NAME_MAPPING

def get_model_info_by_id(model_id: str) -> dict[str, str | float]:
    llm = PRICING_MAPPING[model_id]
    return llm.model_dump()

def get_all_models() -> list[dict[str, str | float]]:
    return list(map(get_model_info_by_id, sorted(PRICING_MAPPING.keys())))

