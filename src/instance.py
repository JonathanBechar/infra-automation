from pydantic import BaseModel, field_validator, Field, ValidationError
from ipaddress import IPv4Address
import sys


class InstanceState(BaseModel):
    Name: str

class Ec2Instances(BaseModel):
    InstanceId: str = Field(min_length=19, max_length=19)
    PublicIpAddress: IPv4Address
    InstanceType: str
    State: InstanceState
    actions: list = Field(default_factory=list)

    @field_validator("InstanceId")
    @classmethod
    def validate_id(cls, value: str) -> str:
        if not value.startswith("i-"):
            raise ValueError("InstanceId must start with i-")
        return value
    
    @field_validator("InstanceType")
    @classmethod
    def validate_type(cls, value: str) -> str:
        allowed = ["t2.micro", "t2.small", "t2.medium"]
        if value not in allowed:
            raise ValueError(f"InstanceType must be one of {allowed}")
        return value
    
    # @field_validator
    # @classmethod
    # def validate_
    # TODO