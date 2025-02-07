from york_genai_calc.models.recurrence import RECURRENCE_OPTIONS

def validate_recurrence(val: str | None) -> str | None:

    if not (val in RECURRENCE_OPTIONS or val is None):
        raise ValueError(f"must be one of {RECURRENCE_OPTIONS}")

    return val