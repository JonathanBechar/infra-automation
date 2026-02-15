import json
from pathlib import Path
from src.logger import setup_logging


# --- LOGGER ---
logger = setup_logging(__name__)


# --- PATH ---
file_path = Path("configs/instances.json")


# --- LOADFILE ---
def load_instances() -> list[dict]:
    try:
        if not file_path.exists():
            logger.info("Data file doesn't exist. Creating new")
            return []
        with open(file_path) as f:
            data = json.load(f)
        logger.info(f"Loaded {len(data)} instances")
    
    except json.JSONDecodeError as e:
        logger.error(f"instances.json is not valid JSON: {e}")
        return []
    
    except Exception as e:
        logger.exception(f"failed to load instances: {e}")
        return []
    
    return data


# --- SAVEDATA ---
def save_instances(instances: list[dict]):
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(instances, f, indent=2)
        logger.info(f"Saved {len(instances)} instances")
    
    except Exception as e:
        logger.exception(f"Failed to save instances: {e}")
        raise


# --- APPEND ---
def append_instances(instance_dict: dict):
    instances = load_instances()
    instances.append(instance_dict)
    save_instances(instances)
    logger.info(f"Appended instance: {instance_dict.get("InstanceId")}")