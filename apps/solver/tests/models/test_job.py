import pytest
from pydantic import ValidationError
from uuid import uuid4, UUID

from job import Job
from delivery_point import DeliveryPoint


def make_depot(**overrides) -> dict:
    defaults = {"name": "Depot", "lat": -23.55, "lng": -46.63}
    return {**defaults, **overrides}


def make_delivery_point(**overrides) -> dict:
    defaults = {"name": "Customer 1", "lat": -23.55, "lng": -46.63, "cargo_weight": 10}
    return {**defaults, **overrides}


def make_job(**overrides) -> dict:
    defaults = {
        "job_id": uuid4(),
        "vehicle": {"max_capacity": 100},
        "depot": make_depot(),
        "delivery_points": [make_delivery_point()],
        # 2x2: depot + 1 delivery point
        "distance_matrix": [
            [0.0, 10.0],
            [10.0, 0.0],
        ],
    }
    return {**defaults, **overrides}


class TestJobCreation:
    def test_valid_job(self):
        job = Job(**make_job())
        assert isinstance(job.job_id, UUID)
        assert len(job.delivery_points) == 1
        assert isinstance(job.delivery_points[0], DeliveryPoint)

    def test_valid_job_multiple_delivery_points(self):
        dp1 = make_delivery_point(name="Customer 1")
        dp2 = make_delivery_point(name="Customer 2")
        job = Job(
            **make_job(
                delivery_points=[dp1, dp2],
                distance_matrix=[
                    [0.0, 10.0, 20.0],
                    [10.0, 0.0, 15.0],
                    [20.0, 15.0, 0.0],
                ],
            )
        )
        assert len(job.delivery_points) == 2

    def test_invalid_job_id_raises(self):
        with pytest.raises(ValidationError):
            Job(**make_job(job_id="not-a-uuid"))

    def test_no_delivery_points_raises(self):
        with pytest.raises(ValidationError, match="delivery_points cannot be empty"):
            Job(**make_job(delivery_points=[], distance_matrix=[[0.0]]))


class TestJobDistanceMatrix:
    def test_empty_distance_matrix_raises(self):
        with pytest.raises(ValidationError, match="distance_matrix cannot be empty"):
            Job(**make_job(distance_matrix=[]))

    def test_non_square_matrix_raises(self):
        with pytest.raises(ValidationError, match="distance_matrix must be square"):
            Job(**make_job(distance_matrix=[[0.0, 10.0, 5.0], [10.0, 0.0]]))

    def test_matrix_size_mismatch_raises(self):
        # 1 delivery point needs 2x2 matrix (depot + 1), but we give 3x3
        with pytest.raises(ValidationError, match="distance_matrix must have 2 rows"):
            Job(
                **make_job(
                    distance_matrix=[
                        [0.0, 1.0, 2.0],
                        [1.0, 0.0, 3.0],
                        [2.0, 3.0, 0.0],
                    ]
                )
            )

    def test_matrix_too_small_raises(self):
        # 1 delivery point needs 2x2, but we give 1x1
        with pytest.raises(ValidationError, match="distance_matrix must have 2 rows"):
            Job(**make_job(distance_matrix=[[0.0]]))

    def test_negative_distance_raises(self):
        with pytest.raises(
            ValidationError, match="distance_matrix values must be non-negative"
        ):
            Job(**make_job(distance_matrix=[[0.0, -1.0], [-1.0, 0.0]]))
