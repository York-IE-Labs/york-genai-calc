from york_genai_calc.models.types import OptionalStr
from york_genai_calc.models.validators import validate_recurrence
from pydantic import BaseModel, field_validator


class ComponentInput(BaseModel):
    component_name: str
    component_index: int
    model_id: str
    n_input_tokens: int
    n_output_tokens: int

    recurrence: OptionalStr = None

    recurrence_validator = field_validator('recurrence')(validate_recurrence)


class ProjectInput(BaseModel):
    project_name: str
    components: list[ComponentInput]