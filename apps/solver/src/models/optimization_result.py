from pydantic import BaseModel
from uuid import UUID
from enum import StrEnum


class OptimizationStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class OptimizationError(BaseModel):
    job_id: UUID
    status: OptimizationStatus = OptimizationStatus.FAILED
    error_message: str
