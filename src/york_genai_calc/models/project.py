from york_genai_calc.models.llm import LLM
from york_genai_calc.models.types import OptionalStr
from york_genai_calc.models.validators import validate_recurrence
from pydantic import BaseModel, field_validator

class Component(BaseModel):

    component_index: int
    component_name: str
    n_input_tokens: int
    n_output_tokens: int

    recurrence: OptionalStr = None

    llm: LLM

    recurrence_validator = field_validator('recurrence')(validate_recurrence)


class Project(BaseModel):

    project_name: str
    components: list[Component]
