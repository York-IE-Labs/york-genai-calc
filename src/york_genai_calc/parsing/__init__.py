from york_genai_calc.mappings.pricing import get_llm_pricing_from_model_id
from york_genai_calc.models.project import Project, Component
from york_genai_calc.models.user_input import ProjectInput, ComponentInput


def validate_user_input(user_input: dict) -> ProjectInput:

    component_defs = user_input['components']

    components = list(map(ComponentInput.model_validate, component_defs))

    project = ProjectInput(
        project_name=user_input['project_name'],
        components=components
    )

    return project

def process_component(component_input: ComponentInput) -> Component:

    return Component(
        component_index=component_input.component_index,
        component_name=component_input.component_name,
        n_input_tokens=component_input.n_input_tokens,
        n_output_tokens=component_input.n_output_tokens,
        llm=get_llm_pricing_from_model_id(component_input.model_id),
        recurrence=component_input.recurrence
    )

def process_project(project_input: ProjectInput) -> Project:

    components = list(map(process_component, project_input.components))

    return Project(
        project_name=project_input.project_name,
        components=components
    )
