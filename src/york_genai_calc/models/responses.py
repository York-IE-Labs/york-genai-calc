from pydantic import BaseModel, field_validator
from york_genai_calc.models.llm import LLM
from york_genai_calc.models.validators import validate_recurrence


class CostCalculation(BaseModel):
    daily_input_cost: float
    weekly_input_cost: float
    monthly_input_cost: float
    yearly_input_cost: float
    one_time_input_cost: float

    daily_output_cost: float
    weekly_output_cost: float
    monthly_output_cost: float
    yearly_output_cost: float
    one_time_output_cost: float

    daily_total_cost: float
    weekly_total_cost: float
    monthly_total_cost: float
    yearly_total_cost: float
    one_time_total_cost: float

class ComponentOutput(BaseModel):
    component_index: int
    component_name: str
    n_input_tokens: int
    n_output_tokens: int
    llm: LLM

    recurrence: str | None
    cost: CostCalculation

    validate_recurrence = field_validator('recurrence')(validate_recurrence)

class ProjectOutput(BaseModel):
    project_name: str
    components: list[ComponentOutput]
    cost: CostCalculation


class Response(BaseModel):
    project: ProjectOutput
    status: int