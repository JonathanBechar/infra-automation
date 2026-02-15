from src.logger import setup_logging


# --- LOGGER ---
logger = setup_logging(__name__)


# --- USERINPUT ---
def get_user_input() -> dict:
    instance = {}
    logger.info("User input started")
    
    try:
        # --- NAME ---
        instance_name = input("Name your instance: ")
        instance["Name"] = instance_name
        logger.debug(f"Instance name set: {instance_name}")
        
        # --- IMAGEID ---
        while True:
            instance_os = input("Enter desired instance OS (Linux/Windows): ").strip().lower()
            if instance_os == "windows":
                instance["ImageId"] = "ami-06b5375e3af24939c"
                break
            if instance_os == "linux":
                while True:
                    ans = input("Choose desired linux instance (Amazon/Ubuntu): ").strip().lower()
                    if ans == "amazon":
                        instance["ImageId"] = "ami-0c1fe732b5494dc14"
                        break
                    elif ans == "ubuntu":
                        instance["ImageId"] = "ami-0b6c6ebed2801a5cb"
                        break
                    else:
                        logger.warning(f"Unsupported OS entered: {instance_os}")
                        continue
                break
            else:
                logger.warning(f"Unsupported OS entered: {instance_os}")
                continue
        logger.info(f"OS set: {instance_os}, ImageId={instance["ImageId"]}")
        logger.debug(f"ImageId chosen: {instance['ImageId']}")
    
        # --- INSTANCETYPE ---
        while True:
            print(
                """Instances Types:
                t2.micro: 1 vCPU, 1 GiB Memory
                t2.small: 1 vCPU, 2 Gib Memory
                t2.medium: 2 vCPU, 4 GiB Memory"""
                )
            instance_type = input("Enter desired instance type: ").strip().lower()
            if instance_type in ["t2.micro", "t2.small", "t2.medium"]:
                instance["InstanceType"] = instance_type
            else:
                logger.warning("Unsupported instance type")
                continue
            logger.info("Instance data recieved")
            logger.debug(f"Final instance dict: {instance}")
            return instance
    
    except KeyboardInterrupt:
        logger.warning("User aborted the program")
        exit("\nQuitting...")
    
    except ValueError as e:
        logger.error(f"Validation error in user input: {e}")
        exit


# --- MAIN ---
if __name__ == "__main__":
    instance = get_user_input()
    print(instance)