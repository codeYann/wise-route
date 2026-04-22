from pydantic import BaseModel, field_validator, model_validator
from .coordinate import Coordinate
from .delivery_point import DeliveryPoint
from .vehicle import Vehicle
from uuid import UUID

from typing import List


class Job(BaseModel):
    job_id: UUID
    vehicle: Vehicle
    depot: Coordinate
    delivery_points: List[DeliveryPoint]
    distance_matrix: List[List[float]]

    @field_validator("delivery_points")
    @classmethod
    def validate_delivery_points(
        cls, value: List[DeliveryPoint]
    ) -> List[DeliveryPoint]:
        if not value:
            raise ValueError("delivery_points cannot be empty")
        return value

    @field_validator("distance_matrix")
    @classmethod
    def validate_distance_matrix(cls, value: List[List[float]]) -> List[List[float]]:
        if not value:
            raise ValueError("distance_matrix cannot be empty")
        length = len(value)
        if any(len(row) != length for row in value):
            raise ValueError("distance_matrix must be square")
        if any(d < 0 for row in value for d in row):
            raise ValueError("distance_matrix values must be non-negative")
        return value

    @model_validator(mode="after")
    def validate_matrix_size(self) -> "Job":
        expected = len(self.delivery_points) + 1  # +1 for the depot
        if len(self.distance_matrix) != expected:
            raise ValueError(f"distance_matrix must have {expected} rows")
        return self
