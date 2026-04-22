from pydantic import field_validator
from .coordinate import Coordinate


class DeliveryPoint(Coordinate):
    cargo_weight: int

    @field_validator("cargo_weight")
    @classmethod
    def validate_cargo_weight(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Cargo weight cannot be negative")
        return value
