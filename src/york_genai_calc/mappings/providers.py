from csv import DictReader
from york_genai_calc.config import paths

with (paths.ASSETS_FOLDER / "providers.csv").open() as f_in:
    PROVIDER_NAME_MAPPING = {
        record['provider_id']: record['provider_name_pretty']
        for record
        in DictReader(f_in)
    }

def get_provider_pretty_name_from_id(provider_id: str) -> str:
    return PROVIDER_NAME_MAPPING[provider_id]
