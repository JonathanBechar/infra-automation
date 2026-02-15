import json
from pydantic import BaseModel, field_validator, Field, ValidationError
from ipaddress import IPv4Address
from src.logger import setup_logging


# --- LOGGER ---
logger = setup_logging(__name__)


# --- INSTANCECLASS ---
class InstanceState(BaseModel):
    Code: int
    Name: str

class Ec2Instances(BaseModel):
    Name: str
    ImageId: str = Field(default_factory=lambda: "ami-0c1fe732b5494dc14")
    InstanceId: str = Field(min_length=19, max_length=19)
    PublicIpAddress: IPv4Address
    InstanceType: str
    VpcId: str
    SubnetId: str
    State: InstanceState
    
    @field_validator("InstanceId")
    @classmethod
    def validate_id(cls, value: str) -> str:
        if not value.startswith("i-"):
            raise ValueError("InstanceId must start with 'i-'")
        return value
    
    @field_validator("InstanceType")
    @classmethod
    def validate_type(cls, value: str) -> str:
        allowed = {"t2.micro", "t2.small", "t2.medium"}
        if value not in allowed:
            raise ValueError(f"InstanceType must be one of {allowed}")
        return value
    
    @field_validator("ImageId")
    @classmethod
    def validate_image_id(cls, value: str) -> str:
        if not value.startswith("ami-"):
            raise ValueError("ImageId must start with 'ami-'")
        return value
    
    @field_validator("VpcId")
    @classmethod
    def validate_vpc_id(cls, value: str) -> str:
        if not value.startswith("vpc-"):
            raise ValueError("VpcId must start with 'vpc-'")
        return value
    
    @field_validator("SubnetId")
    @classmethod
    def validate_subnet_id(cls, value: str) -> str:
        if not value.startswith("subnet-"):
            raise ValueError("SubnetId must start with 'subnet-'")
        return value
