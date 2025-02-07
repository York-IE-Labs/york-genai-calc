from york_genai_calc import parsing
from york_genai_calc.config import constants
from york_genai_calc.models.project import Component
from york_genai_calc.models.recurrence import RecurrenceLiterals
from york_genai_calc.models.responses import ComponentOutput, CostCalculation, ProjectOutput


def calculate_daily_cost(cost: float, recurrence: str | None) -> float:
    match recurrence:
        case RecurrenceLiterals.DAILY:
            return cost
        case RecurrenceLiterals.WEEKLY:
            return cost / constants.DAYS_IN_WEEK
        case RecurrenceLiterals.MONTHLY:
            return cost / constants.DAYS_IN_MONTH
        case RecurrenceLiterals.YEARLY:
            return cost / constants.DAYS_IN_YEAR
        case _:
            return cost

def create_component_cost_calculation(input_cost: float, output_cost: float, recurrence: str | None) -> CostCalculation:
    if recurrence is None:
        return CostCalculation(
            one_time_input_cost=input_cost,
            one_time_output_cost=output_cost,
            one_time_total_cost=input_cost + output_cost,

            daily_input_cost=constants.NONE_COST,
            weekly_input_cost=constants.NONE_COST,
            monthly_input_cost=constants.NONE_COST,
            yearly_input_cost=constants.NONE_COST,

            daily_output_cost=constants.NONE_COST,
            weekly_output_cost=constants.NONE_COST,
            monthly_output_cost=constants.NONE_COST,
            yearly_output_cost=constants.NONE_COST,

            daily_total_cost=constants.NONE_COST,
            weekly_total_cost=constants.NONE_COST,
            monthly_total_cost=constants.NONE_COST,
            yearly_total_cost=constants.NONE_COST,
        )

    daily_input_cost = calculate_daily_cost(input_cost, recurrence)
    daily_output_cost = calculate_daily_cost(output_cost, recurrence)
    daily_total_cost = daily_input_cost + daily_output_cost

    return CostCalculation(
        daily_input_cost=daily_input_cost,
        weekly_input_cost=daily_input_cost * constants.DAYS_IN_WEEK,
        monthly_input_cost=daily_input_cost * constants.DAYS_IN_MONTH,
        yearly_input_cost=daily_input_cost * constants.DAYS_IN_YEAR,

        daily_output_cost=daily_output_cost,
        weekly_output_cost=daily_output_cost * constants.DAYS_IN_WEEK,
        monthly_output_cost=daily_output_cost * constants.DAYS_IN_MONTH,
        yearly_output_cost=daily_output_cost * constants.DAYS_IN_YEAR,

        daily_total_cost=daily_total_cost,
        weekly_total_cost=daily_total_cost * constants.DAYS_IN_WEEK,
        monthly_total_cost=daily_total_cost * constants.DAYS_IN_MONTH,
        yearly_total_cost=daily_total_cost * constants.DAYS_IN_YEAR,

        one_time_input_cost=constants.NONE_COST,
        one_time_output_cost=constants.NONE_COST,
        one_time_total_cost=constants.NONE_COST
    )


def calculate_component_cost(component: Component) -> ComponentOutput:

    input_cost = (component.n_input_tokens / 1_000) * component.llm.cost_per_1k_input_tokens
    output_cost = (component.n_output_tokens / 1_000) * component.llm.cost_per_1k_output_tokens

    return ComponentOutput(
        component_index=component.component_index,
        component_name=component.component_name,
        n_input_tokens=component.n_input_tokens,
        n_output_tokens=component.n_output_tokens,
        llm=component.llm,
        recurrence=component.recurrence,
        cost=create_component_cost_calculation(input_cost, output_cost, recurrence=component.recurrence)
    )


def calculate_project_cost(user_input: dict) -> dict:

    project_input = parsing.validate_user_input(user_input)
    project = parsing.process_project(project_input)

    processed_components: list[ComponentOutput] = list(map(calculate_component_cost, project.components))

    out = ProjectOutput(
        project_name=project.project_name,
        components=sorted(processed_components, key=lambda pc: pc.component_index),
        cost=CostCalculation(
            daily_input_cost=sum(map(lambda pc: pc.cost.daily_input_cost, processed_components)),
            weekly_input_cost=sum(map(lambda pc: pc.cost.weekly_input_cost, processed_components)),
            monthly_input_cost=sum(map(lambda pc: pc.cost.monthly_input_cost, processed_components)),
            yearly_input_cost=sum(map(lambda pc: pc.cost.yearly_input_cost, processed_components)),

            daily_output_cost=sum(map(lambda pc: pc.cost.daily_output_cost, processed_components)),
            weekly_output_cost=sum(map(lambda pc: pc.cost.weekly_output_cost, processed_components)),
            monthly_output_cost=sum(map(lambda pc: pc.cost.monthly_output_cost, processed_components)),
            yearly_output_cost=sum(map(lambda pc: pc.cost.yearly_output_cost, processed_components)),

            daily_total_cost=sum(map(lambda pc: pc.cost.daily_total_cost, processed_components)),
            weekly_total_cost=sum(map(lambda pc: pc.cost.weekly_total_cost, processed_components)),
            monthly_total_cost=sum(map(lambda pc: pc.cost.monthly_total_cost, processed_components)),
            yearly_total_cost=sum(map(lambda pc: pc.cost.yearly_total_cost, processed_components)),

            one_time_input_cost=sum(map(lambda pc: pc.cost.one_time_input_cost, processed_components)),
            one_time_output_cost=sum(map(lambda pc: pc.cost.one_time_output_cost, processed_components)),
            one_time_total_cost=sum(map(lambda pc: pc.cost.one_time_total_cost, processed_components))
        )
    )

    return out.model_dump()
