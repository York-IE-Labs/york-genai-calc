from csv import DictReader
from york_genai_calc.config import paths

with (paths.ASSETS_FOLDER / "models.csv").open() as f_in:
    MODEL_NAME_MAPPING = {
        record['model_id']: record['model_name_pretty']
        for record
        in DictReader(f_in)
    }

def get_model_pretty_name_from_id(model_id: str) -> str:
    return MODEL_NAME_MAPPING[model_id]
