from pydantic import BaseModel, field_validator


class Vehicle(BaseModel):
    max_capacity: int

    @field_validator("max_capacity")
    @classmethod
    def validate_max_capacity(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("max_capacity must be a positive integer")
        return value
