from pydantic import BaseModel
from uuid import UUID
from typing import List

from .optimization_result import OptimizationStatus
from .coordinate import Coordinate


class Waypoint(Coordinate):
    sequence: int
    accumulated_load: float


class RouteSolution(BaseModel):
    job_id: UUID
    status: OptimizationStatus = OptimizationStatus.COMPLETED
    sequence: List[Waypoint]
    total_distance: float
    naive_distance: float
    distance_saved: float
    processing_time_ms: float
