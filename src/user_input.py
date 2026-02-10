import json
from instance import Ec2Instances, InstanceState

def get_user_input():
    instances = {}
    # TODO


def save_data_to_file():
    with open("configs/instances.json", "a") as f:
        data = json.dump(f)
    return data

if __name__ == "__main__":
    get_user_input()
    save_data_to_file()
    # TODO