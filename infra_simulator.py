from src.user_input import get_user_input
from src.generator import enrich_instance
from src.instance import Ec2Instances
from src.save_data import append_instances
from src.logger import setup_logging
from pydantic import ValidationError
from src.subproc import run_bash_script
from argparse import ArgumentParser
import json


logger = setup_logging(__name__)


def list_instances() -> list:
    try:
        with open("configs/instances.json") as f:
            instances = json.load(f)
            return instances
    except json.JSONDecodeError as e:
        logger.error(f"instances.json is not valid JSON: {e}")
        return []


def main_program():
    input_data = get_user_input()
    full_data = enrich_instance(input_data)

    try:
        instance = Ec2Instances.model_validate(full_data)
    except ValidationError as e:
        logger.error(f"{e}")
        return
    
    append_instances(instance.model_dump(mode='json'))
    logger.info('Saved data to "configs/instances.json"')

    run_bash_script()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("command", choices=["create", "list"], help="list - lists all saved instances. create - enables input for instance creation (default)", default="create", nargs="?")
    parser.add_argument("--ids", help="lists instances by their InstanceId", nargs="*")
    args = parser.parse_args()
    print(args)
        
    if args.command == "create":
        main_program()
    
    if args.command == "list":
        instances = list_instances()
        if args.ids:
            ids = args.ids
            ... # TODO
        else:
            for instance in instances:
                print(instance)
