import argparse
import json
import typing

from pathlib import Path
from york_genai_calc import getters
from york_genai_calc.calculate import calculate_project_cost
from york_genai_calc.config.actions import Actions, VALID_ACTIONS


def parse_args() -> argparse.Namespace:

    parent_parser = argparse.ArgumentParser(prog="York GenAI Calculator", add_help=True)
    subparsers = parent_parser.add_subparsers(title="subcommands", help="Calculator Subcommands", required=True)

    estimate_parser = subparsers.add_parser(Actions.ESTIMATE, help="Estimate the cost of project")
    estimate_me_group = estimate_parser.add_mutually_exclusive_group(required=True)
    estimate_me_group.add_argument("-f", "--file", type=Path, help="path to input file")
    estimate_me_group.add_argument('-d', '--data', type=str, help="input json")
    estimate_parser.set_defaults(action=Actions.ESTIMATE)

    ids_parser = subparsers.add_parser(Actions.IDS, help="Fetch all model ids")
    ids_parser.set_defaults(action=Actions.IDS)

    llm_parser = subparsers.add_parser(Actions.LLM, help="Fetch all info for a LLM or all LLMs")
    llm_parser.add_argument("-m", "--model", help="Model id to fetch", required=False, default=None)
    llm_parser.set_defaults(action=Actions.LLM)

    mapping_parser = subparsers.add_parser(Actions.MAPPING, help="Show model or provider mapping")
    mapping_me_group = mapping_parser.add_mutually_exclusive_group(required=True)
    mapping_me_group.add_argument('-m', action="store_true", help="show models")
    mapping_me_group.add_argument('-p', action="store_true", help="show providers")
    mapping_parser.set_defaults(action=Actions.MAPPING)

    return parent_parser.parse_args()


def create_estimate(args: argparse.Namespace) -> dict:

    if args.file:
        with args.file.open() as f_in:
            dat = json.load(f_in)
    else:
        dat = json.loads(args.data)

    return {"estimate": calculate_project_cost(dat)}


def get_ids(args: argparse.Namespace) -> dict:

    return {"ids": getters.get_all_model_ids()}


def get_llm(args: argparse.Namespace) -> dict:

    if args.model:
        return {"models": [getters.get_model_info_by_id(args.model), ]}
    else:
        return {"models": getters.get_all_models()}


def get_mapping(args: argparse.Namespace) -> dict:

    if args.m:
        return {"mapping": getters.get_model_name_mapping()}
    else:
        return {"mapping": getters.get_provider_mapping()}



def arg_handler(args: argparse.Namespace) -> typing.Callable[[argparse.Namespace], dict]:
    match args.action:
        case Actions.ESTIMATE:
            return create_estimate
        case Actions.IDS:
            return get_ids
        case Actions.LLM:
            return get_llm
        case Actions.MAPPING:
            return get_mapping
        case _:
            raise ValueError(f"Invalid argument {args.action}. Valid actions are: {VALID_ACTIONS}")

def main():
    args = parse_args()
    f = arg_handler(args)
    print(json.dumps(f(args), indent=2))
