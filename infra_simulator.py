from src.user_input import get_user_input
from src.generator import enrich_instance
from src.instance import Ec2Instances
from src.save_data import append_instances
from src.logger import setup_logging
from pydantic import ValidationError


logger = setup_logging(__name__)


def main_program():
    print("before")
    input_data = get_user_input()
    print("after")
    full_data = enrich_instance(input_data)

    try:
        instance = Ec2Instances.model_validate(full_data)
    except ValidationError as e:
        logger.error(f"{e}")
        return
    
    append_instances(instance.model_dump(mode='json'))
    logger.info('Saved data to "configs/instances.json"')

if __name__ == "__main__":
        main_program()

