import random


allowed = "0123456789abcdef"
aws_prefixes = [3, 13, 18, 34, 52, 54]

def generate_instance_id() -> str:
    random_nums = "".join(random.choice(allowed) for _ in range(17))
    return "i-" + random_nums



def generate_vpc_id() -> str:
    random_nums = "".join(random.choice(allowed) for _ in range(8))
    return "vpc-" + random_nums


def generate_subnet_id() -> str:
    random_nums = "".join(random.choice(allowed) for _ in range(8))
    return "subnet-" + random_nums


def generate_public_ip() -> str:
    return f"{random.choice(aws_prefixes)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"


def enrich_instance(data: dict) -> dict:
    instance = dict(data)
    instance["InstanceId"] = generate_instance_id()
    instance["VpcId"] = generate_vpc_id()
    instance["SubnetId"] = generate_subnet_id()
    instance["PublicIpAddress"] = generate_public_ip()
    instance["State"] = {"Code": 16, "Name": "running"}
    
    if "ImageId" not in instance:
        instance["ImageId"] = "ami-0c1fe732b5494dc14"
    return instance
    
